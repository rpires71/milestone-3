"""
URL Configuration for Portuguese Kitchen

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Author: Roberto Pires
Date: January 2026

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published, Chapter 6.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views from this package

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Homepage
    path('', views.home, name='home'),
    
    # Placeholder paths for other apps (will be implemented later)
    # path('menu/', include('menu.urls')),
    # path('bookings/', include('bookings.urls')),
    # path('accounts/', include('accounts.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])