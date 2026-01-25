"""
Booking forms for Portuguese Kitchen Booking System.

Author: Roberto Pires
Date: January 2026
"""

from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):
    """
    Form for creating and editing bookings.
    
    Includes validation for:
    - Past dates
    - Guest count limits
    - Required fields
    """
    
    class Meta:
        model = Booking
        fields = [
            'booking_date',
            'timeslot',
            'number_of_guests',
            'special_requests'
        ]
        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': date.today().isoformat()
                }
            ),
            'timeslot': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'number_of_guests': forms.Select(
                attrs={'class': 'form-select'},
                choices=[(i, f'{i} Guest{"s" if i > 1 else ""}') for i in range(1, 9)]
            ),
            'special_requests': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'maxlength': 500,
                    'placeholder': 'Dietary requirements, accessibility needs...'
                }
            ),
        }
    
    def clean_booking_date(self):
        """Validate booking date is not in the past."""
        booking_date = self.cleaned_data.get('booking_date')
        
        if booking_date < date.today():
            raise forms.ValidationError(
                'Booking date cannot be in the past.'
            )
        
        return booking_date
    
    def clean_number_of_guests(self):
        """Validate guest count is within limits."""
        guests = self.cleaned_data.get('number_of_guests')
        
        if guests < 1 or guests > 8:
            raise forms.ValidationError(
                'Number of guests must be between 1 and 8.'
            )
        
        return guests