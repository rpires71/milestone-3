"""
Menu Views Module

This module contains view functions for the menu application in the Portuguese
Kitchen Django project. It handles HTTP requests related to displaying the
restaurant's menu to users browsing the website.

Views in this module:
- menu: Displays the static menu page with Portuguese dishes

Author: Robert Pires
Date: March 2026
"""

from django.shortcuts import render


def menu(request):
    """
    Display the static menu page for Portuguese Kitchen.
    
    This is a simple function-based view that renders the restaurant's menu
    page, showing all available Portuguese dishes organised by category
    (starters, main courses, desserts, and drinks). The menu is currently
    static, meaning the content is hard-coded in the template rather than
    dynamically loaded from a database.
    
    Args:
        request (HttpRequest): The HTTP request object sent by Django when a
            user navigates to the menu page. This object contains metadata about
            the request including:
            - request.method: The HTTP method used (GET, POST, etc.)
            - request.user: The currently authenticated user (or AnonymousUser)
            - request.META: HTTP headers and server information
            - request.GET/POST: Query parameters or form data
    
    Returns:
        HttpResponse: A rendered HTML response containing the menu page. The
            render() function:
            1. Loads the 'menu.html' template from the menu/templates/ directory
            2. Processes any template tags and variables (though none are used
               in this static implementation)
            3. Returns an HttpResponse object with the rendered HTML content
            4. Automatically sets the Content-Type header to 'text/html'
    
    Template:
        menu.html - Located in menu/templates/menu.html
        This template extends base.html and displays:
        - Restaurant menu organised by category
        - Dish names (Portuguese and English)
        - Descriptions of authentic Portuguese ingredients
        - Pricing information
        - High-quality images of dishes (optimised WebP format)
    
    URL Pattern:
        This view is typically mapped to /menu/ in the URL configuration.
        Example in urls.py:
        path('menu/', views.menu, name='menu')
    
    Context Data:
        Currently, this view passes no context data to the template (empty
        context dictionary). In a dynamic implementation, this would include:
        - menu_items: QuerySet of MenuItem objects from the database
        - categories: List of menu categories
        - featured_dishes: Special or seasonal offerings
        - user: Current user (already available via request.context_processors)
    
    Future Enhancements:
        To make this a dynamic, database-driven menu:
        1. Create a MenuItem model with fields (name, description, price, category)
        2. Query the database: menu_items = MenuItem.objects.filter(available=True)
        3. Pass context: return render(request, 'menu.html', {'menu_items': menu_items})
        4. Update template to loop through menu_items using {% for item in menu_items %}
    
    Example Usage:
        # In urls.py
        from menu import views
        
        urlpatterns = [
            path('menu/', views.menu, name='menu'),
        ]
        
        # User navigates to: https://portuguese-kitchen.com/menu/
        # Django calls: menu(request)
        # Returns: Rendered HTML page with restaurant menu
    
    Notes:
        - This is a function-based view (FBV) rather than a class-based view (CBV)
        - FBVs are simpler for straightforward pages like static menus
        - No authentication required - menu is public to all visitors
        - No form processing needed - this is a display-only view
        - Consider adding caching for performance if traffic is high
    
    See Also:
        - bookings.views.booking_page: For the table booking functionality
        - menu/templates/menu.html: The template rendered by this view
        - menu/urls.py: URL configuration mapping /menu/ to this view
    """
    # Render the menu template and return the HTTP response
    # render() is a Django shortcut that combines:
    # 1. loader.get_template('menu.html') - Load the template
    # 2. template.render(context, request) - Render with context
    # 3. HttpResponse(rendered_content) - Create HTTP response
    # All in one convenient function call
    return render(request, 'menu.html')