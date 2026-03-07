# US8: EMAIL CONFIRMATION SYSTEM
# Create this file: bookings/emails.py

"""
Email utility functions for Portuguese Kitchen Booking System.

This module handles sending booking confirmation emails to customers.

Author: Roberto Pires
Date: February 2026
Course: Code Institute - Milestone Project 3

Implements US8: Email confirmation for bookings
"""

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging

# Set up logging for email failures (AC5)
logger = logging.getLogger(__name__)


def send_booking_confirmation_email(booking):
    """
    Send a booking confirmation email to the customer.
    
    Implements US8: Email confirmation with all acceptance criteria.
    
    Args:
        booking: Booking instance with all booking details
        
    Returns:
        bool: True if email sent successfully, False otherwise
        
    Raises:
        Exception: Logs error but doesn't raise (AC5)
    """
    try:
        # Get customer email (AC1, AC2)
        if booking.user:
            recipient_email = booking.user.email
            customer_name = f"{booking.user.first_name} {booking.user.last_name}".strip() or booking.user.username
        else:
            # Guest booking
            recipient_email = booking.guest_email
            customer_name = booking.guest_name
        
        # Validate email exists
        if not recipient_email:
            logger.error(f"No email address for booking {booking.reference_number}")
            return False
        
        # Email subject (AC2, AC3)
        subject = f'Booking Confirmation - {booking.reference_number} - Portuguese Kitchen'
        
        # Prepare context for email template (AC2, AC4)
        context = {
            'booking': booking,
            'customer_name': customer_name,
            'restaurant_name': 'Portuguese Kitchen',
            'restaurant_address': '45 Brick Lane, London, UK, E1 6PU',
            'restaurant_phone': '+44 (0) 207 123 4567',
            'restaurant_email': 'info@portuguesekitchen.co.uk',
        }
        
        # Render HTML email template (AC3, AC7)
        html_message = render_to_string('emails/booking_confirmation.html', context)
        
        # Create plain text version (AC7 - accessibility)
        plain_message = strip_tags(html_message)
        
        # Alternative: Use custom plain text template for better formatting
        try:
            plain_message = render_to_string('emails/booking_confirmation.txt', context)
        except:
            # Fallback to stripped HTML if plain text template doesn't exist
            plain_message = strip_tags(html_message)
        
        # Send email with both HTML and plain text (AC3, AC7, AC8)
        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,  # Plain text version (fallback)
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
        )
        
        # Attach HTML version
        email.attach_alternative(html_message, "text/html")
        
        # Send email (AC1, AC8 - immediate delivery)
        email.send(fail_silently=False)
        
        # Log success
        logger.info(f"Confirmation email sent successfully for booking {booking.reference_number} to {recipient_email}")
        
        return True
        
    except Exception as e:
        # AC5: Handle email delivery failure
        # Log error but don't break the booking process
        logger.error(
            f"Failed to send confirmation email for booking {booking.reference_number}: {str(e)}",
            exc_info=True
        )
        return False


def send_booking_update_email(booking, change_type='updated'):
    """
    Send email notification when a booking is updated or cancelled.
    
    Args:
        booking: Booking instance
        change_type: Type of change ('updated', 'cancelled')
        
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Get customer email
        if booking.user:
            recipient_email = booking.user.email
            customer_name = f"{booking.user.first_name} {booking.user.last_name}".strip() or booking.user.username
        else:
            recipient_email = booking.guest_email
            customer_name = booking.guest_name
        
        if not recipient_email:
            logger.error(f"No email address for booking {booking.reference_number}")
            return False
        
        # Email subject based on change type
        if change_type == 'cancelled':
            subject = f'Booking Cancelled - {booking.reference_number} - Portuguese Kitchen'
            template_html = 'emails/booking_cancelled.html'
            template_txt = 'emails/booking_cancelled.txt'
        else:
            subject = f'Booking Updated - {booking.reference_number} - Portuguese Kitchen'
            template_html = 'emails/booking_updated.html'
            template_txt = 'emails/booking_updated.txt'
        
        # Prepare context
        context = {
            'booking': booking,
            'customer_name': customer_name,
            'restaurant_name': 'Portuguese Kitchen',
            'restaurant_address': '45 Brick Lane, London, UK, E1 6PU',
            'restaurant_phone': '+44 (0) 207 123 4567',
            'restaurant_email': 'info@portuguesekitchen.co.uk',
        }
        
        # Render templates
        try:
            html_message = render_to_string(template_html, context)
            plain_message = render_to_string(template_txt, context)
        except:
            # Fallback if specific templates don't exist
            html_message = render_to_string('emails/booking_confirmation.html', context)
            plain_message = strip_tags(html_message)
        
        # Send email
        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
        )
        
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)
        
        logger.info(f"Update email sent successfully for booking {booking.reference_number}")
        return True
        
    except Exception as e:
        logger.error(
            f"Failed to send update email for booking {booking.reference_number}: {str(e)}",
            exc_info=True
        )
        return False