"""
Booking views for Portuguese Kitchen Booking System.

This module handles all booking-related views including:
- Displaying the booking form
- Checking table availability
- Creating new bookings
- Managing booking confirmations

Author: Roberto Pires
Date: January 2026
Course: Code Institute - Milestone Project 3
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import Booking, TimeSlot, Table
from .forms import BookingForm
from django.http import HttpResponse
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta, date
from collections import Counter
import csv
import json


def booking_page(request):
    """
    Display the booking form page.
    
    GET: Show empty booking form
    POST: Process booking submission
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered booking template with form context
        
    Template: booking.html
    Context:
        - form: BookingForm instance
        - today: Current date for minimum date validation
    """
    if request.method == 'POST':
        # Pass current user to form for authentication check
        form = BookingForm(request.POST, user=request.user)
        
        if form.is_valid():
            booking = form.save(commit=False)
            
            # Generate unique reference number
            booking.reference_number = booking.generate_reference_number()
            
            
            # Set initial status
            booking.status = 'Pending'
            
            # Save booking
            booking.save()
            
            # Success message
            messages.success(
                request,
                f'Booking confirmed! Your reference number is {booking.reference_number}'
            )
            
            # Redirect to confirmation page
            return redirect('bookings:confirmation', reference=booking.reference_number)
        else:
            # Form has errors
            messages.error(
                request,
                'There was an error with your booking. Please check the form and try again.'
            )
    else:
        # Pass current user to form
        form = BookingForm(user=request.user)
    
    context = {
        'form': form,
        'today': date.today().isoformat(),
    }
    
    return render(request, 'booking.html', context)


def check_availability(request):
    """
    AJAX endpoint to check table availability for selected date, time, and party size.
    
    Args:
        request: HTTP request with GET parameters:
            - booking_date: Date in YYYY-MM-DD format
            - timeslot_id: TimeSlot ID
            - number_of_guests: Party size (1-8)
    
    Returns:
        JsonResponse with:
            - available (bool): Whether tables are available
            - message (str): User-friendly message
            - capacity_remaining (int): Remaining capacity (optional)
    
    Reference: Vincent (2020), Chapter 9 - RESTful APIs
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        # Extract parameters
        booking_date_str = request.GET.get('booking_date')
        timeslot_id = request.GET.get('timeslot_id')
        number_of_guests = int(request.GET.get('number_of_guests', 0))
        
        # Validate parameters
        if not all([booking_date_str, timeslot_id, number_of_guests]):
            return JsonResponse({
                'available': False,
                'message': 'Missing required parameters'
            }, status=400)
        
        # Parse date
        booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d').date()
        
        # Check if date is in the past
        if booking_date < date.today():
            return JsonResponse({
                'available': False,
                'message': 'Cannot book tables for past dates'
            })
        
        # Get timeslot
        try:
            timeslot = TimeSlot.objects.get(id=timeslot_id, is_active=True)
        except TimeSlot.DoesNotExist:
            return JsonResponse({
                'available': False,
                'message': 'Invalid time slot selected'
            })
        
        # Check available capacity
        available_capacity = timeslot.get_available_capacity(booking_date)
        
        if available_capacity >= number_of_guests:
            return JsonResponse({
                'available': True,
                'message': f'Table available for {number_of_guests} guests!',
                'capacity_remaining': available_capacity
            })
        else:
            return JsonResponse({
                'available': False,
                'message': f'Sorry, only {available_capacity} seats available for this time slot. Please select another time.',
                'capacity_remaining': available_capacity
            })
            
    except ValueError as e:
        return JsonResponse({
            'available': False,
            'message': 'Invalid date format. Please use YYYY-MM-DD.'
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'available': False,
            'message': 'An error occurred while checking availability. Please try again.'
        }, status=500)


def get_timeslots(request):
    """
    AJAX endpoint to retrieve available time slots for a specific date.
    
    Args:
        request: HTTP request with GET parameter:
            - date: Date in YYYY-MM-DD format
    
    Returns:
        JsonResponse with array of timeslot objects:
            - id: TimeSlot ID
            - time: Time in HH:MM format
            - display_time: Formatted time (e.g., "7:00 PM")
            - available_capacity: Remaining capacity
    
    Reference: Vincent (2020), Chapter 9 - RESTful APIs
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        date_str = request.GET.get('date')
        
        if not date_str:
            return JsonResponse({'error': 'Date parameter required'}, status=400)
        
        # Parse date
        booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Get all active time slots
        timeslots = TimeSlot.objects.filter(is_active=True).order_by('time')
        
        # Build response data
        timeslot_data = []
        for slot in timeslots:
            available_capacity = slot.get_available_capacity(booking_date)
            
            timeslot_data.append({
                'id': slot.id,
                'time': slot.time.strftime('%H:%M'),
                'display_time': slot.time.strftime('%I:%M %p'),
                'available_capacity': available_capacity,
                'is_available': available_capacity > 0
            })
        
        return JsonResponse({'timeslots': timeslot_data})
        
    except ValueError:
        return JsonResponse({
            'error': 'Invalid date format. Please use YYYY-MM-DD.'
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'error': 'An error occurred while loading time slots.'
        }, status=500)


def booking_confirmation(request, reference):
    """
    Display booking confirmation page with booking details.
    
    Args:
        request: HTTP request object
        reference: Unique booking reference number
        
    Returns:
        Rendered confirmation template
        
    Template: booking_confirmation.html
    Context:
        - booking: Booking instance
    
    Reference: Vincent (2020), Chapter 4 - Views
    """
    try:
        booking = Booking.objects.get(reference_number=reference)
        
         # AC5: Verify user ownership for authenticated bookings
        if booking.user and request.user.is_authenticated:
            if booking.user != request.user:
                messages.error(request, 'You can only view your own bookings.')
                return redirect('bookings:my_bookings')
        
        # Guest bookings (no user) remain accessible via reference

        context = {
            'booking': booking,
        }
        
        return render(request, 'booking_confirmation.html', context)
        
    except Booking.DoesNotExist:
        messages.error(request, 'Booking not found.')
        return redirect('home')


@login_required
def my_bookings(request):
    """
    Display user's booking history (requires authentication).
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered bookings list template
        
    Template: my_bookings.html
    Context:
        - upcoming_bookings: Future bookings (ordered by date)
        - past_bookings: Previous bookings (ordered by date desc)
    
    Reference: Vincent (2020), Chapter 8 - User Authentication
    """
    today = date.today()
    
    # Get upcoming bookings
    upcoming_bookings = Booking.objects.filter(
        user=request.user,
        booking_date__gte=today
    ).exclude(
        status='Cancelled'
    ).order_by('booking_date', 'timeslot__time')
    
    # Get past bookings
    past_bookings = Booking.objects.filter(
        user=request.user,
        booking_date__lt=today
    ).order_by('-booking_date', '-timeslot__time')
    
    context = {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
    }
    
    return render(request, 'my_bookings.html', context)

@login_required
def edit_booking(request, reference):
    """
    Edit an existing booking.
    
    Implements US2-AC8: Re-validates capacity when guest count changes.
    
    Only allows editing of:
    - Bookings owned by the current user
    - Future bookings (not past dates)
    - Non-cancelled bookings
    
    Args:
        request: HTTP request object
        reference: Booking reference number
        
    Returns:
        Rendered edit template or redirect to my_bookings
        
    Template: edit_booking.html
    Context:
        - form: Pre-filled BookingForm
        - booking: Original booking instance
    """
    # Get booking or 404
    booking = get_object_or_404(Booking, reference_number=reference)
    
    # Security check: Only owner can edit
    if booking.user != request.user:
        messages.error(request, 'You can only edit your own bookings.')
        return redirect('bookings:my_bookings')
    
    # Validation: Can't edit past bookings
    if booking.booking_date < date.today():
        messages.error(request, 'You cannot edit past bookings.')
        return redirect('bookings:my_bookings')
    
    # Validation: Can't edit cancelled bookings
    if booking.status == 'Cancelled':
        messages.error(request, 'You cannot edit cancelled bookings.')
        return redirect('bookings:my_bookings')
    
    if request.method == 'POST':
        # Create form with POST data and existing instance
        form = BookingForm(request.POST, instance=booking, user=request.user)
        
        if form.is_valid():
            # Save updates
            updated_booking = form.save(commit=False)
            
            # ===== AC8: CAPACITY RE-VALIDATION =====
            # Check if guest count changed
            if updated_booking.number_of_guests != booking.number_of_guests:
                # Calculate available capacity (excluding current booking)
                other_guests = Booking.objects.filter(
                    booking_date=updated_booking.booking_date,
                    timeslot=updated_booking.timeslot,
                    status__in=['Pending', 'Confirmed', 'Seated']
                ).exclude(id=booking.id).aggregate(
                    Sum('number_of_guests')
                )['number_of_guests__sum'] or 0
                
                # Get total capacity from tables
                total_capacity = Table.objects.filter(
                    is_available=True
                ).aggregate(Sum('capacity'))['capacity__sum'] or 40
                
                available_capacity = total_capacity - other_guests
                
                # Prevent overbooking
                if available_capacity < updated_booking.number_of_guests:
                    messages.error(
                        request,
                        f'Cannot update to {updated_booking.number_of_guests} guests. '
                        f'Only {available_capacity} seats available for this time slot. '
                        f'Please choose a different time or reduce party size.'
                    )
                    context = {
                        'form': form,
                        'booking': booking,
                        'is_edit': True,
                    }
                    return render(request, 'edit_booking.html', context)
            # ===== END CAPACITY RE-VALIDATION =====
            
            # Ensure user remains the same (security)
            updated_booking.user = request.user
            
            # Keep original reference number
            updated_booking.reference_number = booking.reference_number
            
            # Save to database
            updated_booking.save()
            
            # Success message
            messages.success(
                request,
                f'Booking {booking.reference_number} updated successfully!'
            )
            
            # Redirect to confirmation page
            return redirect('bookings:confirmation', reference=booking.reference_number)
        else:
            # Form has errors
            messages.error(
                request,
                'There was an error updating your booking. Please check the form.'
            )
    else:
        # GET request: Pre-fill form with existing data
        form = BookingForm(instance=booking, user=request.user)
    
    context = {
        'form': form,
        'booking': booking,
        'is_edit': True,
    }
    
    return render(request, 'edit_booking.html', context)


@login_required
def cancel_booking(request, reference):
    """
    Cancel an existing booking.
    
    Updates booking status to 'Cancelled' and records cancellation timestamp.
    Only allows cancellation of:
    - Bookings owned by the current user
    - Future bookings (not past dates)
    - Non-cancelled bookings
    
    Args:
        request: HTTP request object
        reference: Booking reference number
        
    Returns:
        Redirect to my_bookings page with success/error message
        
    Security:
        - Requires POST method to prevent accidental cancellation
        - Checks user ownership
        - Validates booking is future and not already cancelled
    """
    # Only accept POST requests (security - prevents accidental cancellation via URL)
    if request.method != 'POST':
        messages.error(request, 'Invalid request method.')
        return redirect('bookings:my_bookings')
    
    # Get booking or 404
    booking = get_object_or_404(Booking, reference_number=reference)
    
    # Security check: Only owner can cancel
    if booking.user != request.user:
        messages.error(request, 'You can only cancel your own bookings.')
        return redirect('bookings:my_bookings')
    
    # Validation: Can't cancel past bookings
    if booking.booking_date < date.today():
        messages.error(request, 'You cannot cancel past bookings.')
        return redirect('bookings:my_bookings')
    
    # Validation: Can't cancel already cancelled bookings
    if booking.status == 'Cancelled':
        messages.warning(request, 'This booking is already cancelled.')
        return redirect('bookings:my_bookings')
    
    # Cancel the booking using model method
    booking.cancel()
    
    # Success message
    messages.success(
        request,
        f'Booking {booking.reference_number} has been cancelled successfully.'
    )
    
    # Redirect to my bookings
    return redirect('bookings:my_bookings')

def get_available_timeslots(request):
    """
    AJAX endpoint to fetch available time slots for a given date.
    Implements: US1-AC3, AC4, AC5, AC8
    """
    if request.method != 'GET':
        return JsonResponse({'error': True, 'message': 'Method not allowed'}, status=405)
    
    try:
        # Get parameters
        date_str = request.GET.get('date')
        guests = int(request.GET.get('guests', 1))
        
        # Validate parameters
        if not date_str:
            return JsonResponse({
                'error': True,
                'message': 'Please select a date first',
                'timeslots': []
            })
        
        # Parse date
        booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Check if date is in the past
        if booking_date < date.today():
            return JsonResponse({
                'error': True,
                'message': 'Cannot book for past dates',
                'timeslots': []
            })
        
        # Get active time slots ordered by time
        all_timeslots = TimeSlot.objects.filter(
            is_active=True
        ).order_by('time')
        
        available_timeslots = []
        
        # Check capacity for each time slot
        for timeslot in all_timeslots:
            # Get total capacity
            total_capacity = timeslot.max_capacity
            
            # Get existing bookings
            existing_bookings = Booking.objects.filter(
                booking_date=booking_date,
                timeslot=timeslot,
                status__in=['Pending', 'Confirmed', 'Seated']
            ).aggregate(
                total_guests=Sum('number_of_guests')
            )
            
            booked_guests = existing_bookings['total_guests'] or 0
            available_capacity = total_capacity - booked_guests
            
            # Only include if enough capacity
            if available_capacity >= guests:
                available_timeslots.append({
                    'id': timeslot.id,
                    'time': timeslot.time.strftime('%H:%M'),
                    'display_time': timeslot.time.strftime('%I:%M %p'),
                    'available_capacity': available_capacity,
                    'is_available': True
                })
        
        # User feedback
        if not available_timeslots:
            date_formatted = booking_date.strftime('%B %d, %Y')
            guest_text = f'{guests} guest{"s" if guests > 1 else ""}'
            message = f'No time slots available for {guest_text} on {date_formatted}. Please try a different date or reduce party size.'
        else:
            slot_count = len(available_timeslots)
            message = f'{slot_count} time slot{"s" if slot_count > 1 else ""} available'
        
        return JsonResponse({
            'error': False,
            'message': message,
            'timeslots': available_timeslots,
            'date': date_str,
            'guests': guests
        })
        
    except ValueError:
        return JsonResponse({
            'error': True,
            'message': 'Invalid date format',
            'timeslots': []
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'error': True,
            'message': f'Error: {str(e)}',
            'timeslots': []
        }, status=500)
    
@staff_member_required
def staff_dashboard(request):
    """
    Staff dashboard showing bookings with search functionality.
    
    Implements:
    - US11: View all bookings for today
    - US12: Search bookings by name
    
    Access:
        - Restricted to staff/admin users only (US11-AC1, US12-AC1)
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered staff dashboard template
        
    Template: staff_dashboard.html
    Context:
        - today: Current date
        - bookings: Filtered bookings (today's or search results)
        - search_query: Current search term
        - is_search: Whether showing search results
        - total_guests: Total number of guests
        - total_bookings: Count of bookings
    """
    # Get today's date (US11-AC2, US11-AC8)
    today = date.today()
    
    # Get search query (US12-AC2)
    search_query = request.GET.get('search', '').strip()
    
    # Base queryset with optimizations (US12-AC9)
    base_queryset = Booking.objects.select_related(
        'user', 'timeslot', 'table'
    )
    
    # Determine if we're searching or showing today's bookings
    is_search = bool(search_query)
    
    if is_search:
        # Search functionality (US12-AC3, AC4, AC5)
        bookings = base_queryset.filter(
            Q(user__first_name__icontains=search_query) |  # Case-insensitive (AC3)
            Q(user__last_name__icontains=search_query) |   # Partial match (AC4)
            Q(user__username__icontains=search_query) |
            Q(guest_name__icontains=search_query) |        # Guest bookings
            Q(reference_number__icontains=search_query)    # Bonus: search by reference
        ).order_by('-booking_date', 'timeslot__time')
        
    else:
        # Default: Show today's bookings (US11-AC2)
        bookings = base_queryset.filter(
            booking_date=today
        ).order_by('timeslot__time', 'created_at')
    
    # Calculate statistics
    total_bookings = bookings.count()
    
    # Total expected guests (excluding cancelled)
    total_guests = bookings.filter(
        status__in=['Pending', 'Confirmed', 'Seated']
    ).aggregate(
        Sum('number_of_guests')
    )['number_of_guests__sum'] or 0
    
    # Group bookings by status for quick overview
    pending_count = bookings.filter(status='Pending').count()
    confirmed_count = bookings.filter(status='Confirmed').count()
    cancelled_count = bookings.filter(status='Cancelled').count()
    completed_count = bookings.filter(status='Completed').count()
    
    context = {
        'today': today,
        'bookings': bookings,
        'search_query': search_query,
        'is_search': is_search,
        'total_bookings': total_bookings,
        'total_guests': total_guests,
        'pending_count': pending_count,
        'confirmed_count': confirmed_count,
        'cancelled_count': cancelled_count,
        'completed_count': completed_count,
    }
    
    return render(request, 'staff_dashboard.html', context)

@staff_member_required
def booking_statistics(request):
    """
    Admin-only booking statistics dashboard with analytics and insights.
    
    Implements US17: View booking statistics to analyze restaurant usage patterns.
    
    Access:
        - Restricted to staff/admin users only (AC1)
    
    Features:
        - Date range filtering (AC3)
        - Core metrics display (AC4)
        - Usage pattern insights (AC5)
        - Status breakdown (AC6)
        - CSV export (AC12)
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered statistics template or CSV download
    """
    # Check if export requested (AC12)
    export_format = request.GET.get('export')
    
    # Get date range parameters (AC3)
    date_range = request.GET.get('range', '30')  # Default: last 30 days
    
    # Calculate date range
    today = date.today()
    
    if date_range == '7':
        start_date = today - timedelta(days=7)
        range_label = 'Last 7 Days'
    elif date_range == '30':
        start_date = today - timedelta(days=30)
        range_label = 'Last 30 Days'
    elif date_range == '90':
        start_date = today - timedelta(days=90)
        range_label = 'Last 90 Days'
    elif date_range == 'custom':
        # Custom date range (AC3)
        start_str = request.GET.get('start_date')
        end_str = request.GET.get('end_date')
        
        if start_str and end_str:
            start_date = datetime.strptime(start_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_str, '%Y-%m-%d').date()
        else:
            start_date = today - timedelta(days=30)
            end_date = today
        
        range_label = f'{start_date.strftime("%b %d, %Y")} - {end_date.strftime("%b %d, %Y")}'
    else:
        start_date = today - timedelta(days=30)
        end_date = today
        range_label = 'Last 30 Days'
    
    # Set end_date if not custom
    if date_range != 'custom':
        end_date = today
    
    # Base queryset with date filtering (AC3, AC11 - optimized)
    bookings = Booking.objects.filter(
        booking_date__gte=start_date,
        booking_date__lte=end_date
    ).select_related('user', 'timeslot')
    
    # Handle no data scenario (AC8)
    if not bookings.exists():
        context = {
            'has_data': False,
            'range_label': range_label,
            'date_range': date_range,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'booking_statistics.html', context)
    
    # AC4: Core Metrics
    total_bookings = bookings.count()
    
    # Total guests (sum of party sizes)
    total_guests = bookings.aggregate(
        total=Sum('number_of_guests')
    )['total'] or 0
    
    # Cancelled bookings
    cancelled_count = bookings.filter(status='Cancelled').count()
    
    # Completed bookings
    completed_count = bookings.filter(status='Completed').count()
    
    # Confirmed bookings
    confirmed_count = bookings.filter(status='Confirmed').count()
    
    # Pending bookings
    pending_count = bookings.filter(status='Pending').count()
    
    # Average party size
    avg_party_size = round(total_guests / total_bookings, 1) if total_bookings > 0 else 0
    
    # AC6: Status Breakdown
    status_breakdown = bookings.values('status').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Convert to dict for easier template access
    status_dict = {item['status']: item['count'] for item in status_breakdown}
    
    # AC5: Usage Pattern Insights - Bookings by Day of Week
    day_of_week_data = []
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for booking in bookings:
        day_num = booking.booking_date.weekday()
        day_of_week_data.append(day_names[day_num])
    
    day_counts = Counter(day_of_week_data)
    day_of_week_chart = [
        {'day': day, 'count': day_counts.get(day, 0)}
        for day in day_names
    ]
    
    # AC5: Usage Pattern Insights - Bookings by Time Slot
    timeslot_data = bookings.values(
        'timeslot__time'
    ).annotate(
        count=Count('id')
    ).order_by('timeslot__time')
    
    timeslot_chart = [
        {
            'time': item['timeslot__time'].strftime('%I:%M %p') if item['timeslot__time'] else 'Unknown',
            'count': item['count']
        }
        for item in timeslot_data
    ]
    
    # Daily trend (for line chart)
    daily_bookings = bookings.values('booking_date').annotate(
        count=Count('id')
    ).order_by('booking_date')
    
    daily_trend = [
        {
            'date': item['booking_date'].strftime('%Y-%m-%d'),
            'date_display': item['booking_date'].strftime('%b %d'),
            'count': item['count']
        }
        for item in daily_bookings
    ]
    
    # Most popular booking times
    top_timeslots = list(timeslot_data[:5])  # Top 5
    
    # Busiest day of week
    busiest_day = max(day_of_week_chart, key=lambda x: x['count'])
    
    # AC12: CSV Export
    if export_format == 'csv':
        return export_statistics_csv(
            bookings, 
            start_date, 
            end_date, 
            range_label,
            total_bookings,
            total_guests,
            status_dict
        )
    
    # Prepare context (AC2, AC7, AC9)
    context = {
        'has_data': True,
        'range_label': range_label,
        'date_range': date_range,
        'start_date': start_date,
        'end_date': end_date,
        
        # AC4: Core Metrics
        'total_bookings': total_bookings,
        'total_guests': total_guests,
        'cancelled_count': cancelled_count,
        'completed_count': completed_count,
        'confirmed_count': confirmed_count,
        'pending_count': pending_count,
        'avg_party_size': avg_party_size,
        
        # AC6: Status Breakdown
        'status_breakdown': status_breakdown,
        
        # AC5: Usage Patterns
        'day_of_week_chart': day_of_week_chart,
        'timeslot_chart': timeslot_chart,
        'daily_trend': daily_trend,
        
        # Additional insights
        'busiest_day': busiest_day,
        'top_timeslots': top_timeslots,
        
        # For charts (JSON)
        'day_of_week_json': json.dumps(day_of_week_chart),
        'timeslot_json': json.dumps(timeslot_chart),
        'daily_trend_json': json.dumps(daily_trend),
    }
    
    return render(request, 'booking_statistics.html', context)


def export_statistics_csv(bookings, start_date, end_date, range_label, total_bookings, total_guests, status_dict):
    """
    Export booking statistics to CSV format.
    
    Implements US17-AC12: Export statistics in CSV format.
    """
    # Create HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="booking_statistics_{start_date}_to_{end_date}.csv"'
    
    writer = csv.writer(response)
    
    # Summary section
    writer.writerow(['Booking Statistics Report'])
    writer.writerow(['Date Range', range_label])
    writer.writerow(['Generated', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    writer.writerow([])
    
    # Core metrics
    writer.writerow(['SUMMARY METRICS'])
    writer.writerow(['Metric', 'Value'])
    writer.writerow(['Total Bookings', total_bookings])
    writer.writerow(['Total Guests', total_guests])
    writer.writerow(['Confirmed Bookings', status_dict.get('Confirmed', 0)])
    writer.writerow(['Pending Bookings', status_dict.get('Pending', 0)])
    writer.writerow(['Cancelled Bookings', status_dict.get('Cancelled', 0)])
    writer.writerow(['Completed Bookings', status_dict.get('Completed', 0)])
    writer.writerow([])
    
    # Detailed bookings
    writer.writerow(['DETAILED BOOKINGS'])
    writer.writerow(['Reference', 'Date', 'Time', 'Customer', 'Guests', 'Status', 'Special Requests'])
    
    for booking in bookings:
        customer_name = ''
        if booking.user:
            customer_name = f"{booking.user.first_name} {booking.user.last_name}".strip()
            if not customer_name:
                customer_name = booking.user.username
        else:
            customer_name = booking.guest_name or 'Guest'
        
        writer.writerow([
            booking.reference_number,
            booking.booking_date.strftime('%Y-%m-%d'),
            booking.timeslot.time.strftime('%I:%M %p') if booking.timeslot else 'N/A',
            customer_name,
            booking.number_of_guests,
            booking.status,
            booking.special_requests or ''
        ])
    
    return response