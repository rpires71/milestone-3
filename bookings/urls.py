"""
URL Configuration for Bookings Application.

This module defines URL patterns for all booking-related views.

Author: Roberto Pires
Date: January 2026
Course: Code Institute - Milestone Project 3
"""

from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    # Booking form page
    path('', views.booking_page, name='booking'),
    
    # AJAX endpoints
    path('api/check-availability/', views.check_availability, name='check_availability'),
    path('api/get-timeslots/', views.get_timeslots, name='get_timeslots'),
    
    # Booking confirmation
    path('confirmation/<str:reference>/', views.booking_confirmation, name='confirmation'),
    
    # User booking management (requires login)
    path('my-bookings/', views.my_bookings, name='my_bookings'),

    # User booking editing/updating (requires login)
    path('edit/<str:reference>/', views.edit_booking, name='edit_booking'),

    # User booking cancellation (requires login)
    path('cancel/<str:reference>/', views.cancel_booking, name='cancel_booking'),

    # AJAX endpoint for available time slots - ADD THIS LINE
    path('api/available-timeslots/', views.get_available_timeslots, name='available_timeslots'),
    
     # Staff Dashboard (US11)
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),

]












































































































