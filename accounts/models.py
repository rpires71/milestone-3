"""
Customer Profile Model

This module defines the CustomerProfile model which extends Django's built-in
User model to store additional customer-specific information for the Portuguese
Kitchen booking system.

The one-to-one relationship pattern follows Django best practices for extending
the User model without modifying the core authentication system (Vincent, 2020,
Chapter 8).

"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerProfile(models.Model):
    """
    Extended user profile model for restaurant customers.
    
    This model extends Django's built-in User model using a one-to-one
    relationship, allowing storage of customer-specific information without
    modifying the core User model (Vincent, 2020, Chapter 8).
    
    The profile stores dietary requirements and special requests which are
    used to personalise the booking experience and ensure customer needs
    are communicated to restaurant staff.
    
    Attributes:
        user (OneToOneField): Link to Django's User model. Each user has
            exactly one profile. Cascade deletion ensures profiles are
            removed when users are deleted.
        dietary_requirements (TextField): Free-text field for customers to
            specify dietary requirements, allergies, or preferences (e.g.,
            "Vegetarian", "Gluten intolerance", "Nut allergy").
        special_requests (TextField): Default special requests that are
            pre-filled when customers make new bookings (e.g., "Window
            seat preferred", "Quiet table").
        created_at (DateTimeField): Timestamp recording when the profile
            was created. Automatically set on first save and never changed.
    
    Meta:
        verbose_name: Human-readable singular name for Django admin interface.
        verbose_name_plural: Human-readable plural name for Django admin.
        ordering: Profiles ordered by creation date, newest first.
    
    Methods:
        __str__: Returns a string representation showing the linked username.
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 8.
    """
    
    # One-to-One relationship with Django's User model
    # Using CASCADE means if a User is deleted, their profile is also deleted
    # This maintains referential integrity (Vincent, 2020, Chapter 8)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile',
        help_text="Linked user account"
    )
    
    # TextField allows unlimited text storage for detailed dietary information
    # blank=True allows the field to be empty in forms
    # null=True allows NULL values in the database
    # Following Django convention for optional text fields (Vincent, 2020, Chapter 4)
    dietary_requirements = models.TextField(
        blank=True,
        null=True,
        help_text="Customer's dietary requirements or allergies"
    )
    
    # Special requests field for default preferences that apply to all bookings
    # This reduces repetitive data entry for regular customers
    special_requests = models.TextField(
        blank=True,
        null=True,
        help_text="Default special requests for bookings"
    )
    
    # Timestamp fields for audit trail and record keeping
    # auto_now_add=True sets the timestamp once when the record is created
    # This cannot be changed afterwards (Vincent, 2020, Chapter 4)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Profile creation timestamp"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines how the model appears in Django's admin interface and
        the default ordering for querysets (Vincent, 2020, Chapter 5).
        """
        verbose_name = "Customer Profile"
        verbose_name_plural = "Customer Profiles"
        # Order profiles by creation date, newest first (indicated by minus sign)
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of the CustomerProfile instance.
        
        Returns a human-readable string used in the Django admin interface
        and when the model is printed. Following Django best practice of
        providing meaningful __str__ methods (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Formatted string showing the linked username.
        
        Example:
            >>> profile = CustomerProfile.objects.get(id=1)
            >>> str(profile)
            'Profile for john_smith'
        """
        return f"Profile for {self.user.username}"


# Django Signals for automatic profile creation
# Signals allow decoupled applications to get notified when actions occur
# elsewhere in the framework (Django Software Foundation, 2024)

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to automatically create a CustomerProfile when a User is created.
    
    This signal handler uses Django's post_save signal to automatically create
    a CustomerProfile whenever a new User account is created. This ensures that
    every user has an associated profile without requiring manual creation
    (Django Software Foundation, 2024).
    
    The 'created' parameter is True only when a new User is created (not when
    an existing User is updated), ensuring profiles are only created once.
    
    Args:
        sender (Model): The model class (User) that sent the signal.
        instance (User): The actual User instance that was saved.
        created (bool): True if a new record was created, False if updated.
        **kwargs: Additional keyword arguments passed by the signal.
    
    Returns:
        None
    
    Example:
        When a new user registers:
        >>> user = User.objects.create_user('john', 'john@example.com', 'password')
        # Signal automatically creates: CustomerProfile(user=user)
    
    References:
        Django Software Foundation (2024) Django documentation: Signals. Available
            at: https://docs.djangoproject.com/en/4.2/topics/signals/
            (Accessed: 17 January 2026).
    """
    if created:
        # Only create profile for new users, not for updates
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the CustomerProfile when the User is saved.
    
    This signal handler ensures the CustomerProfile is saved whenever the
    associated User is saved. This maintains synchronisation between the
    User and CustomerProfile models (Django Software Foundation, 2024).
    
    Note: This signal fires on every User save, including updates. The
    profile must exist before this can execute, which is guaranteed by
    the create_customer_profile signal above.
    
    Args:
        sender (Model): The model class (User) that sent the signal.
        instance (User): The actual User instance that was saved.
        **kwargs: Additional keyword arguments passed by the signal.
    
    Returns:
        None
    
    Example:
        When user details are updated:
        >>> user = User.objects.get(username='john')
        >>> user.email = 'newemail@example.com'
        >>> user.save()
        # Signal automatically saves the associated CustomerProfile
    
    References:
        Django Software Foundation (2024) Django documentation: Signals. Available
            at: https://docs.djangoproject.com/en/4.2/topics/signals/
            (Accessed: 17 January 2026).
    """
    # Save the profile associated with this user
    # This ensures profile changes are persisted to the database
    instance.customer_profile.save()