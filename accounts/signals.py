"""
Signals for Portuguese Kitchen Accounts App.

Automatically creates CustomerProfile when User is created.

Author: Roberto Pires
Date: January 2026
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CustomerProfile


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """
    Create CustomerProfile automatically when User is created.
    
    Args:
        sender: User model
        instance: User instance
        created: Boolean - True if new user
        **kwargs: Additional arguments
    """
    if created:
        CustomerProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    """
    Save CustomerProfile when User is saved.
    
    Creates profile if it doesn't exist (safety check).
    
    Args:
        sender: User model
        instance: User instance
        **kwargs: Additional arguments
    """
    # Use get_or_create to prevent duplicate errors
    profile, created = CustomerProfile.objects.get_or_create(user=instance)
    
    # Only save if profile already existed (not just created)
    if not created:
        profile.save()