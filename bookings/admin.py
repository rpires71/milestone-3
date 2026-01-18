"""
Django Admin Configuration for Bookings Application

This module configures the Django admin interface for Table, TimeSlot, and
Booking models, providing comprehensive booking management tools for staff.

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published, Chapter 5.
"""

from django.contrib import admin
from .models import Table, TimeSlot, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin configuration for Table model.
    
    Provides tools for managing restaurant tables including capacity,
    location, and availability status (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'table_number',
        'capacity',
        'location',
        'is_available',
    ]
    
    # Fields that can be edited directly from list view
    list_editable = [
        'is_available',
    ]
    
    # Filters in the right sidebar
    list_filter = [
        'location',
        'is_available',
        'capacity',
    ]
    
    # Fields that can be searched
    search_fields = [
        'table_number',
        'description',
    ]
    
    # Order tables by table number
    ordering = ['table_number']


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    """
    Admin configuration for TimeSlot model.
    
    Provides tools for managing available booking time slots and capacity
    limits (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'time',
        'max_capacity',
        'is_active',
    ]
    
    # Fields that can be edited directly from list view
    list_editable = [
        'max_capacity',
        'is_active',
    ]
    
    # Filters in the right sidebar
    list_filter = [
        'is_active',
    ]
    
    # Order slots chronologically
    ordering = ['time']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Booking model.
    
    Provides comprehensive booking management interface with search,
    filtering, and status management capabilities (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'reference_number',
        'user',
        'booking_date',
        'timeslot',
        'number_of_guests',
        'table',
        'status',
        'created_at',
    ]
    
    # Fields that can be edited directly from list view
    list_editable = [
        'status',
        'table',
    ]
    
    # Filters in the right sidebar
    list_filter = [
        'status',
        'booking_date',
        'timeslot',
        'created_at',
    ]
    
    # Fields that can be searched
    search_fields = [
        'reference_number',
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    ]
    
    # Read-only fields (cannot be edited)
    readonly_fields = [
        'reference_number',
        'created_at',
        'updated_at',
        'cancelled_at',
    ]
    
    # Fields displayed in the detail/edit view, organised into sections
    fieldsets = (
        ('Booking Information', {
            'fields': (
                'reference_number',
                'user',
                'booking_date',
                'timeslot',
                'number_of_guests',
            )
        }),
        ('Assignment', {
            'fields': (
                'table',
                'status',
            )
        }),
        ('Additional Information', {
            'fields': (
                'special_requests',
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at',
                'cancelled_at',
            ),
            'classes': ('collapse',),  # Collapsible section
        }),
    )
    
    # Order bookings by date (newest first)
    ordering = ['-booking_date', '-timeslot__time']
    
    # Number of bookings per page
    list_per_page = 25

