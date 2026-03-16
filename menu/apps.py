"""
Menu App Configuration

This module configures the menu application for the Portuguese Kitchen
Django project. It defines how Django should initialise and manage the
menu app, which handles the display and organisation of the restaurant's
Portuguese cuisine offerings.

Author: Robert Pires
Date: March 2026
"""

from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Configuration class for the menu application.
    
    This class tells Django how to configure the menu app, which manages
    the presentation of Portuguese Kitchen's food and beverage offerings
    to customers browsing the website.
    
    The menu app handles:
    - Display of menu items organised by category (starters, mains, desserts, drinks)
    - Presentation of authentic Portuguese dishes with descriptions
    - Pricing information for all menu offerings
    - Menu item images and visual presentation
    - Integration with the booking system (allowing customers to view the
      menu before making a reservation)
    
    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary
            key to use for models in this app. BigAutoField uses 64-bit integers,
            supporting a range from -9,223,372,036,854,775,808 to 
            9,223,372,036,854,775,807. This is significantly larger than the
            standard AutoField's 32-bit range (approximately 2 billion records),
            ensuring the database can handle extensive menu item catalogues
            without reaching ID limits.
        name (str): The Python path to the application. Must match the app
            directory name (menu/) and the entry in the INSTALLED_APPS setting
            in settings.py. Django uses this name to locate templates in
            menu/templates/ and static files in menu/static/.
    
    Note:
        This configuration uses single quotes for string literals, which is
        a valid Python style choice. Django accepts both single (') and double (")
        quotes for string values. The important thing is consistency within
        your codebase.
        
        This configuration does not override the ready() method, meaning no
        signal handlers or startup initialisation tasks are registered for this
        app. If future functionality requires automated tasks (such as automatically
        updating menu item availability based on stock levels), the ready()
        method should be implemented here.
    
    Example:
        In settings.py, this app is registered as:
        
        INSTALLED_APPS = [
            ...
            'menu',  # This matches the 'name' attribute below
            ...
        ]
    """
    
    # Use BigAutoField for all model primary keys in this app
    # BigAutoField: 64-bit integer supporting over 9 quintillion unique records
    # vs AutoField: 32-bit integer supporting approximately 2 billion records
    # For a menu system that may include seasonal items, specials, archived
    # dishes, and frequent updates, BigAutoField prevents potential ID exhaustion
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The application name - must match the menu directory and INSTALLED_APPS
    # Django uses this to:
    # 1. Locate templates in menu/templates/menu/
    # 2. Find static files in menu/static/menu/
    # 3. Identify the app in admin interface and management commands
    # 4. Namespace URLs (e.g., {% url 'menu:menu_list' %})
    name = 'menu'