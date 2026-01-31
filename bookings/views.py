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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, date
from .models import Booking, TimeSlot, Table
from .forms import BookingForm


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