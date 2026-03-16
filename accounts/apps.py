"""
Accounts App Configuration

This module configures the accounts application for the Portuguese Kitchen
Django project. It defines how Django should initialise and manage the
accounts app, including signal registration for automated user-related tasks.

"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the accounts application.
    
    This class tells Django how to configure the accounts app, including
    which auto-generated primary key field type to use and the app's name
    within the project.
    
    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary
            key to use for models in this app. BigAutoField supports larger
            integer ranges than the standard AutoField, allowing for more
            database records before hitting integer limits.
        name (str): The Python path to the application. Must match the app
            name in INSTALLED_APPS setting.
    """
    
    # Use BigAutoField for all model primary keys in this app
    # BigAutoField: 64-bit integer (range: -9223372036854775808 to 9223372036854775807)
    # vs AutoField: 32-bit integer (range: -2147483648 to 2147483647)
    default_auto_field = "django.db.models.BigAutoField"
    
    # The application name - must match the app directory name and INSTALLED_APPS
    name = "accounts"

    def ready(self):
        """
        Perform initialization tasks when the app is ready.
        
        This method is called by Django once the app registry is fully populated
        and all models have been imported. It's the appropriate place to register
        signal handlers, which need to connect to models that might not exist
        until all apps are loaded.
        
        Signal registration:
        Importing accounts.signals connects signal handlers (such as post_save
        or pre_delete) to Django's signal framework. These handlers can perform
        automated tasks like:
        - Creating related objects when a user is created (e.g., user profiles)
        - Sending welcome emails after user registration
        - Cleaning up related data when a user is deleted
        - Logging user actions for audit trails
        
        Note:
            The import statement is placed inside ready() rather than at the
            module level to avoid potential circular import issues and to ensure
            signals are only registered once, even if the app is loaded multiple
            times during testing or in certain deployment scenarios.
        
        Raises:
            ImportError: If the accounts.signals module cannot be found or
                contains syntax errors.
        """
        # Import signal handlers to register them with Django's signal dispatcher
        # This must be done here (not at module top) to avoid circular imports
        # and ensure models are fully loaded before signals connect to them
        import accounts.signals  # noqa: F401 (imported but unused - intentional for side effects)