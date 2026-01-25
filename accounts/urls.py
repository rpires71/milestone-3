"""
URL Configuration for Accounts Application.

This module defines URL patterns for authentication views.

Author: Roberto Pires
Date: January 2026
Course: Code Institute - Milestone Project 3
"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Registration
    path('register/', views.register_view, name='register'),
    
    # Login/Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile
    path('profile/', views.profile_view, name='profile'),
    
    # Password Reset
    path('password-reset/', views.password_reset_request, name='password_reset'),
    
    # AJAX endpoints for validation
    path('api/check-username/', views.check_username, name='check_username'),
    path('api/check-email/', views.check_email, name='check_email'),
]