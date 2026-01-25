"""
Authentication forms for Portuguese Kitchen Booking System.

This module defines forms for:
- User registration
- User profile updates
- Login (uses Django's built-in AuthenticationForm)

Author: Roberto Pires
Date: January 2026
Course: Code Institute - Milestone Project 3

Reference: Vincent, W. S. (2020) Django for beginners. Chapter 8.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerProfile


class UserRegistrationForm(UserCreationForm):
    """
    Extended user registration form.
    
    Includes additional fields:
    - Email (required)
    - First name (required)
    - Last name (required)
    
    Validates:
    - Username uniqueness
    - Email uniqueness
    - Password strength
    - Password confirmation match
    """
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
    )
    
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'John'
        })
    )
    
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Smith'
        })
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            })
        }
    
    def __init__(self, *args, **kwargs):
        """
        Customize form initialization.
        
        Adds Bootstrap classes to password fields
        and customizes help text.
        """
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a strong password'
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
        
        # Customize help text
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    
    def clean_email(self):
        """
        Validate email uniqueness.
        
        Returns:
            str: Validated email address
            
        Raises:
            ValidationError: If email already exists
        """
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email address is already registered. Please use a different email or login.'
            )
        
        return email
    
    def clean_username(self):
        """
        Validate username requirements.
        
        Returns:
            str: Validated username
            
        Raises:
            ValidationError: If username doesn't meet requirements
        """
        username = self.cleaned_data.get('username')
        
        # Check minimum length
        if len(username) < 3:
            raise forms.ValidationError(
                'Username must be at least 3 characters long.'
            )
        
        # Check if username exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'This username is already taken. Please choose another.'
            )
        
        return username


class UserProfileForm(forms.ModelForm):
    """
    Form for updating customer profile information.
    
    Includes:
    - Dietary requirements
    - Default special requests
    
    Excludes:
    - User (read-only relationship)
    - Created timestamp
    """
    
    dietary_requirements = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'e.g., Vegetarian, Gluten-free, Nut allergy...'
        }),
        help_text='Let us know about any dietary restrictions or allergies.'
    )
    
    special_requests = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'e.g., Prefer window seating, celebrating anniversary...'
        }),
        help_text='Default requests that will be pre-filled when making bookings.'
    )
    
    class Meta:
        model = CustomerProfile
        fields = ['dietary_requirements', 'special_requests']
    
    def clean_dietary_requirements(self):
        """
        Validate and clean dietary requirements text.
        
        Returns:
            str: Cleaned dietary requirements
        """
        dietary_requirements = self.cleaned_data.get('dietary_requirements', '')
        
        # Trim whitespace
        dietary_requirements = dietary_requirements.strip()
        
        # Limit length (optional validation)
        if len(dietary_requirements) > 500:
            raise forms.ValidationError(
                'Dietary requirements must be 500 characters or less.'
            )
        
        return dietary_requirements
    
    def clean_special_requests(self):
        """
        Validate and clean special requests text.
        
        Returns:
            str: Cleaned special requests
        """
        special_requests = self.cleaned_data.get('special_requests', '')
        
        # Trim whitespace
        special_requests = special_requests.strip()
        
        # Limit length (optional validation)
        if len(special_requests) > 500:
            raise forms.ValidationError(
                'Special requests must be 500 characters or less.'
            )
        
        return special_requests


class LoginForm(forms.Form):
    """
    Custom login form.
    
    (Alternative to Django's AuthenticationForm)
    Allows login with username or email.
    """
    
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or email',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    def clean(self):
        """
        Validate login credentials.
        
        Allows authentication with either username or email.
        
        Returns:
            dict: Cleaned form data
            
        Raises:
            ValidationError: If credentials are invalid
        """
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username_or_email and password:
            # Try to find user by username or email
            from django.contrib.auth import authenticate
            
            # First try username
            user = authenticate(username=username_or_email, password=password)
            
            # If not found, try email
            if user is None:
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is None:
                raise forms.ValidationError(
                    'Invalid username/email or password.'
                )
            
            self.cleaned_data['user'] = user
        
        return self.cleaned_data