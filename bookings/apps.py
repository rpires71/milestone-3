"""
Bookings App Configuration

This module configures the bookings application for the Portuguese Kitchen
Django project. It defines how Django should initialise and manage the
bookings app, which handles all table reservation functionality including
booking creation, modification, cancellation, and availability management.

"""

from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Configuration class for the bookings application.
    
    This class tells Django how to configure the bookings app, which is the
    core functionality of the Portuguese Kitchen restaurant booking system.
    The configuration specifies the type of auto-generated primary key field
    to use for all models within this application.
    
    The bookings app manages:
    - Table reservations (guest and authenticated user bookings)
    - Time slot management and availability checking
    - Booking confirmations and reference codes
    - Staff dashboard for booking administration
    - Booking statistics and analytics
    
    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary
            key to use for models in this app. BigAutoField uses 64-bit integers,
            supporting a range from -9,223,372,036,854,775,808 to 
            9,223,372,036,854,775,807, which is significantly larger than the
            standard AutoField's 32-bit range. This future-proofs the database
            for high-volume booking scenarios.
        name (str): The Python path to the application. Must match the app
            directory name and the entry in the INSTALLED_APPS setting in
            settings.py.
    
    Note:
        This configuration does not override the ready() method, meaning no
        signal handlers or startup tasks are registered for this app. If signal
        registration is needed in future (e.g., for sending booking confirmation
        emails automatically), the ready() method should be implemented here.
    """
    
    # Use BigAutoField for all model primary keys in this app
    # BigAutoField: 64-bit integer supporting over 9 quintillion unique records
    # vs AutoField: 32-bit integer supporting approximately 2 billion records
    # For a busy restaurant, BigAutoField prevents potential ID exhaustion
    default_auto_field = "django.db.models.BigAutoField"
    
    # The application name - must match the bookings directory and INSTALLED_APPS
    # Django uses this to locate templates in bookings/templates/ and
    # static files in bookings/static/
    name = "bookings"