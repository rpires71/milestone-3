"""
Django Admin Configuration for Accounts Application

This module configures the Django admin interface for the CustomerProfile model,
providing staff with tools to view and manage customer profiles.

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published, Chapter 5.
"""

from django.contrib import admin
from .models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for CustomerProfile model.
    
    Provides a customised admin interface for viewing and managing customer
    profiles, including search, filtering, and display options (Vincent, 2020,
    Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'user',
        'created_at',
        'has_dietary_requirements',
        'has_special_requests',
    ]
    
    # Fields that can be searched
    search_fields = [
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    ]
    
    # Filters in the right sidebar
    list_filter = [
        'created_at',
    ]
    
    # Read-only fields (cannot be edited)
    readonly_fields = [
        'user',
        'created_at',
    ]
    
    # Fields displayed in the detail/edit view
    fields = [
        'user',
        'dietary_requirements',
        'special_requests',
        'created_at',
    ]
    
    # Order profiles by newest first
    ordering = ['-created_at']
    
    def has_dietary_requirements(self, obj):
        """
        Display whether profile has dietary requirements.
        
        Args:
            obj (CustomerProfile): The profile instance.
        
        Returns:
            bool: True if dietary requirements exist, False otherwise.
        """
        return bool(obj.dietary_requirements)
    
    # Display as checkmark/cross in admin
    has_dietary_requirements.boolean = True
    has_dietary_requirements.short_description = 'Has Dietary Requirements'
    
    def has_special_requests(self, obj):
        """
        Display whether profile has special requests.
        
        Args:
            obj (CustomerProfile): The profile instance.
        
        Returns:
            bool: True if special requests exist, False otherwise.
        """
        return bool(obj.special_requests)
    
    # Display as checkmark/cross in admin
    has_special_requests.boolean = True
    has_special_requests.short_description = 'Has Special Requests'

