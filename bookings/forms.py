"""
Booking forms for Portuguese Kitchen Booking System.

Author: Roberto Pires
Date: January 2026
"""

from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Booking, TimeSlot


class BookingForm(forms.ModelForm):
    """
    Form for creating a new restaurant booking.
    
    Fields:
        - booking_date: Date of booking
        - timeslot: Selected time slot
        - number_of_guests: Party size (1-8)
        - special_requests: Optional special requests
    
    Validation:
        - Date must be today or in the future
        - Number of guests must be 1-8
        - Time slot must be active
    """
    
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': date.today().isoformat(),
        }),
        label='Booking Date',
        help_text='Select your preferred date'
    )
    
    timeslot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.filter(is_active=True).order_by('time'),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        label='Time Slot',
        help_text='Select your preferred time',
        empty_label='Please select a time'
    )
    
    number_of_guests = forms.IntegerField(
        min_value=1,
        max_value=8,
        widget=forms.Select(
            choices=[(i, f'{i} {"Guest" if i == 1 else "Guests"}') for i in range(1, 9)],
            attrs={'class': 'form-select'}
        ),
        label='Number of Guests',
        help_text='How many people? (Maximum 8)',
        initial=2
    )
    
    special_requests = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any dietary requirements, allergies, or special occasions? (Optional)',
            'maxlength': 500,
        }),
        label='Special Requests',
        help_text='Optional - Maximum 500 characters'
    )
    
    # Guest booking fields (optional - for non-authenticated users)
    guest_name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your full name',
        }),
        label='Full Name',
        help_text='Required for guest bookings'
    )
    
    guest_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
        }),
        label='Email Address',
        help_text='We\'ll send your confirmation here'
    )
    
    guest_phone = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+44 1234 567890',
        }),
        label='Phone Number',
        help_text='In case we need to contact you'
    )
    
    class Meta:
        model = Booking
        fields = [
            'booking_date',
            'timeslot',
            'number_of_guests',
            'special_requests'
        ]
    
    def __init__(self, *args, **kwargs):
        """
        Initialize form and set dynamic attributes.
        
        Args:
            user: Current user (if authenticated)
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # If user is not authenticated, make guest fields required
        if not self.user or not self.user.is_authenticated:
            self.fields['guest_name'].required = True
            self.fields['guest_email'].required = True
            self.fields['guest_phone'].required = True
    
    def clean_booking_date(self):
        """
        Validate that booking date is not in the past.
        
        Returns:
            date: Validated booking date
            
        Raises:
            ValidationError: If date is in the past
        """
        booking_date = self.cleaned_data.get('booking_date')
        
        if booking_date and booking_date < date.today():
            raise ValidationError(
                'Booking date cannot be in the past. Please select today or a future date.'
            )
        
        return booking_date
    
    def clean_number_of_guests(self):
        """
        Validate number of guests is within acceptable range.
        
        Returns:
            int: Validated number of guests
            
        Raises:
            ValidationError: If number is out of range
        """
        number_of_guests = self.cleaned_data.get('number_of_guests')
        
        if number_of_guests and (number_of_guests < 1 or number_of_guests > 8):
            raise ValidationError(
                'Number of guests must be between 1 and 8. For larger parties, please call us.'
            )
        
        return number_of_guests
    
    def clean(self):
        """
        Perform cross-field validation.
        
        Validates:
        - Time slot availability for selected date and party size
        - Guest information if user is not authenticated
        
        Returns:
            dict: Cleaned form data
            
        Raises:
            ValidationError: If validation fails
        """
        cleaned_data = super().clean()
        
        booking_date = cleaned_data.get('booking_date')
        timeslot = cleaned_data.get('timeslot')
        number_of_guests = cleaned_data.get('number_of_guests')
        
        # Check availability if all required fields are present
        if booking_date and timeslot and number_of_guests:
            available_capacity = timeslot.get_available_capacity(booking_date)
            
            if available_capacity < number_of_guests:
                raise ValidationError(
                    f'Sorry, only {available_capacity} seats available for this time slot. '
                    f'Please select a different time or reduce party size.'
                )
        
        # Validate guest information for non-authenticated users
        if not self.user or not self.user.is_authenticated:
            guest_name = cleaned_data.get('guest_name')
            guest_email = cleaned_data.get('guest_email')
            guest_phone = cleaned_data.get('guest_phone')
            
            if not all([guest_name, guest_email, guest_phone]):
                raise ValidationError(
                    'Please provide your name, email, and phone number to complete your booking.'
                )
        
        return cleaned_data
    
    def save(self, commit=True):
        """
        Save the booking instance.
        
        For guest bookings, stores guest information.
        For authenticated users, links to user account.
        
        Args:
            commit: Whether to save to database immediately
            
        Returns:
            Booking: The booking instance
        """
        booking = super().save(commit=False)
        
        # For guest bookings, store guest information
        if not self.user or not self.user.is_authenticated:
            booking.guest_name = self.cleaned_data.get('guest_name')
            booking.guest_email = self.cleaned_data.get('guest_email')
            booking.guest_phone = self.cleaned_data.get('guest_phone')
        else:
            # For authenticated users, link to user account
            booking.user = self.user
        
        if commit:
            booking.save()
        
        return booking

