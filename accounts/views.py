"""
Authentication views for Portuguese Kitchen Booking System.

This module handles user authentication including:
- User registration
- Login/logout
- Password reset
- User profile management

Author: Roberto Pires
Date: January 2026
Course: Code Institute - Milestone Project 3

Reference: Vincent, W. S. (2020) Django for beginners. Chapter 8.
"""

from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from bookings.models import Booking
from .forms import UserRegistrationForm, UserProfileForm
from .models import CustomerProfile
from datetime import date, timezone, timezone

def register_view(request):
    """
    Handle user registration.
    
    GET: Display registration form
    POST: Process registration and create user account
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered registration template or redirect to login
        
    Template: register.html
    Context:
        - form: UserRegistrationForm instance
        
    Reference: Vincent (2020), Chapter 8 - User Authentication
    """
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            # Create user
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            
            # CustomerProfile is created automatically via signals
            
            # Log the user in
            login(request, user)
            
            messages.success(
                request,
                f'Welcome {user.first_name}! Your account has been created successfully.'
            )
            
            # Redirect to home or next URL
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(
                request,
                'Please correct the errors below.'
            )
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'register.html', context)


def login_view(request):
    """
    Handle user login.
    
    GET: Display login form
    POST: Authenticate user and create session
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered login template or redirect after successful login
        
    Template: login.html
    Context:
        - form: AuthenticationForm instance
        
    Reference: Vincent (2020), Chapter 8 - User Authentication
    """
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login successful
            login(request, user)
            
            # Set session expiry
            if not remember:
                # Session expires when browser closes
                request.session.set_expiry(0)
            else:
                # Session expires after 2 weeks
                request.session.set_expiry(1209600)
            
            messages.success(request, f'Welcome back, {user.first_name}!')
            
            # Redirect to next URL or home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(
                request,
                'Invalid username or password. Please try again.'
            )
    
    form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'login.html', context)


@login_required
def logout_view(request):
    """
    Handle user logout.
    
    Args:
        request: HTTP request object
        
    Returns:
        Redirect to home page
        
    Reference: Vincent (2020), Chapter 8 - User Authentication
    """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    """
    Display and update user profile.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered profile template
        
    Template: profile.html
    Context:
        - user: Current user object
        - profile: CustomerProfile instance
        - form: UserProfileForm instance
        
    Reference: Vincent (2020), Chapter 8 - User Authentication
    """
    # Get or create customer profile
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        
        # Also update user first_name and last_name
        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        
        if form.is_valid():
            form.save()
            request.user.save()
            
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    
    # Get user's booking statistics
    from bookings.models import Booking
    from datetime import date
    today = date.today()

    total_bookings = Booking.objects.filter(user=request.user).count()
    
    upcoming_bookings = Booking.objects.filter(
        user=request.user,
        booking_date__gte=today
    ).exclude(status='Cancelled').count()

    completed_count = Booking.objects.filter(
        user=request.user,
        booking_date__lt=today,
        status='Confirmed'
    ).count()

    cancelled_count = Booking.objects.filter(
        user=request.user,
        status='Cancelled'
    ).count()
    
    context = {
        'user': request.user,
        'profile': profile,
        'form': form,
        'total_bookings': total_bookings,
        'upcoming_bookings': upcoming_bookings,
        'completed_count': completed_count,
        'cancelled_count': cancelled_count,
    }
    
    return render(request, 'profile.html', context)


def password_reset_request(request):
    """
    Handle password reset request.
    
    (Placeholder for email-based password reset)
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered password reset template
        
    Template: password_reset.html
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Check if user exists
        try:
            user = User.objects.get(email=email)
            messages.info(
                request,
                'Password reset instructions have been sent to your email.'
            )
            # In production, send actual email here
            return redirect('accounts:login')
        except User.DoesNotExist:
            messages.error(request, 'No account found with that email address.')
    
    return render(request, 'password_reset.html')


# Helper function for checking if username exists (AJAX)
from django.http import JsonResponse

def check_username(request):
    """
    AJAX endpoint to check if username is available.
    
    Args:
        request: HTTP request with GET parameter 'username'
        
    Returns:
        JsonResponse with availability status
    """
    username = request.GET.get('username', '')
    
    if len(username) < 3:
        return JsonResponse({
            'available': False,
            'message': 'Username must be at least 3 characters.'
        })
    
    exists = User.objects.filter(username=username).exists()
    
    return JsonResponse({
        'available': not exists,
        'message': 'Username is available' if not exists else 'Username already taken'
    })


def check_email(request):
    """
    AJAX endpoint to check if email is already registered.
    
    Args:
        request: HTTP request with GET parameter 'email'
        
    Returns:
        JsonResponse with availability status
    """
    email = request.GET.get('email', '')
    
    if not email:
        return JsonResponse({
            'available': False,
            'message': 'Please enter an email address.'
        })
    
    exists = User.objects.filter(email=email).exists()
    
    return JsonResponse({
        'available': not exists,
        'message': 'Email is available' if not exists else 'Email already registered'
    })