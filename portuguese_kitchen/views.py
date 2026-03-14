"""
Main Application Views

This module contains the core views for the Portuguese Kitchen website,
including the homepage and other main site pages.

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published, Chapter 6.
"""

from django.shortcuts import render


def home(request):
    """
    Homepage view.
    
    Displays the main landing page with restaurant information, features,
    and calls-to-action for viewing the menu and making bookings.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Rendered homepage template.
    
    Template:
        index.html
    
    Context:
        None - Static content only.
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 6.
    """
    return render(request, 'index.html')

def menu(request):
    """Display the static menu page."""
    return render(request, 'menu.html')

"""
Custom error handlers for Portuguese Kitchen.
"""

def custom_404(request, exception):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error handler."""
    return render(request, '500.html', status=500)