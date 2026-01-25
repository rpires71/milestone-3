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
]












































































































