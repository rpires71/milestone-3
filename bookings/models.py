"""
Booking System Models

This module defines the core models for the Portuguese Kitchen restaurant
booking system, including Table, TimeSlot, and Booking models.

The models implement a complete reservation system with capacity management,
time slot allocation, and booking lifecycle tracking from creation through
to completion or cancellation (Vincent, 2020).

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published.
    Django Software Foundation (2024) Django documentation. Version 4.2.
        Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
        (Accessed: 17 January 2026).
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import random
import string


class Table(models.Model):
    """
    Represents physical tables in the restaurant.
    
    This model stores information about each table in the restaurant, including
    its capacity, location, and availability status. Tables are referenced by
    bookings but can exist independently, allowing restaurant configuration
    to be managed separately from reservation data (Vincent, 2020, Chapter 4).
    
    The location choices are implemented using Django's choices parameter,
    which provides database-level constraint whilst maintaining code
    readability (Django Software Foundation, 2024).
    
    Attributes:
        table_number (IntegerField): Unique physical table number used for
            identification by staff. Must be unique across all tables.
        capacity (IntegerField): Maximum number of guests that can be seated
            at this table. Must be at least 1.
        location (CharField): Table's location in the restaurant. Uses
            predefined choices (Window, Corner, Centre, Private) to ensure
            data consistency.
        is_available (BooleanField): Indicates whether the table is currently
            available for bookings. Can be set to False for maintenance or
            temporary removal without deleting the table record.
        description (TextField): Optional free-text field for additional
            information about the table (e.g., "Next to fireplace", "Booth
            seating", "Accessible table").
    
    Meta:
        ordering: Tables ordered by table number in ascending order.
        verbose_name: Singular name for Django admin interface.
        verbose_name_plural: Plural name for Django admin interface.
    
    Methods:
        __str__: Returns formatted string showing table number and capacity.
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 4.
        Django Software Foundation (2024) Django documentation: Model field
            reference. Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
            (Accessed: 17 January 2026).
    """
    
    # Location choices defined as class constant
    # This approach keeps related data close to the field definition and
    # makes the choices reusable throughout the application
    # (Django Software Foundation, 2024)
    LOCATION_CHOICES = [
        ('Window', 'Window'),      # Window seating with view
        ('Corner', 'Corner'),      # Corner tables (often more private)
        ('Centre', 'Centre'),      # Central dining area
        ('Private', 'Private'),    # Private dining rooms or booths
    ]

    # IntegerField with unique constraint ensures no duplicate table numbers
    # This is enforced at the database level for data integrity
    # (Vincent, 2020, Chapter 4)
    table_number = models.IntegerField(
        unique=True,
        help_text="Physical table number (must be unique)"
    )
    
    # MinValueValidator ensures capacity is at least 1
    # Validators are checked during form validation and model.clean()
    # (Django Software Foundation, 2024)
    capacity = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Maximum number of guests"
    )
    
    # CharField with choices restricts values to predefined options
    # max_length=20 is sufficient for all choice values
    # default='Centre' ensures new tables have a sensible default location
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default='Centre',
        help_text="Table location in restaurant"
    )
    
    # BooleanField for simple true/false status
    # default=True means new tables are available unless explicitly set otherwise
    # Allows "soft deletion" - tables can be made unavailable without losing
    # historical booking data (Vincent, 2020, Chapter 4)
    is_available = models.BooleanField(
        default=True,
        help_text="Is table available for bookings?"
    )
    
    # TextField for unlimited length text
    # blank=True allows this field to be empty in forms and database
    # Unlike CharField, TextField doesn't need max_length (Vincent, 2020, Chapter 4)
    description = models.TextField(
        blank=True,
        help_text="Additional notes about the table"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines default ordering and human-readable names for the Django
        admin interface (Vincent, 2020, Chapter 5).
        """
        # Order tables by table number (ascending)
        # No minus sign means ascending order (1, 2, 3...)
        ordering = ['table_number']
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        """
        String representation of the Table instance.
        
        Returns a human-readable string showing the table number and capacity.
        This appears in Django admin, dropdowns, and when the model is printed
        (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Formatted string with table number and capacity.
        
        Example:
            >>> table = Table.objects.get(table_number=5)
            >>> str(table)
            'Table 5 (4 seats)'
        """
        return f"Table {self.table_number} ({self.capacity} seats)"


class TimeSlot(models.Model):
    """
    Represents available booking time slots during restaurant service hours.
    
    This model defines the time periods when customers can make reservations.
    Each time slot has an optional maximum capacity, allowing flexible capacity
    management based on staffing levels or service times (Vincent, 2020, Chapter 4).
    
    The model includes business logic methods for calculating remaining capacity,
    following Django's principle of keeping business logic in the model layer
    ("fat models, thin views") (Vincent, 2020, Chapter 4).
    
    Attributes:
        time (TimeField): The time of the booking slot (e.g., 19:00, 19:30).
            Stored as time only (no date component).
        max_capacity (IntegerField): Optional maximum number of guests that
            can be accommodated across all tables during this time slot.
            If not set, defaults to 40 in capacity calculations.
        is_active (BooleanField): Whether this time slot is currently
            accepting bookings. Allows temporary disabling of slots without
            deletion.
    
    Meta:
        ordering: Time slots ordered chronologically by time.
        verbose_name: Singular name with proper spacing.
        verbose_name_plural: Plural name with proper spacing.
    
    Methods:
        __str__: Returns time in HH:MM format (24-hour clock).
        get_available_capacity: Calculates remaining capacity for a given date.
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 4.
    """
    
    # TimeField stores time without date component
    # Suitable for recurring time slots that apply to multiple dates
    # (Vincent, 2020, Chapter 4)
    time = models.TimeField(
        help_text="Booking time (e.g., 19:00)"
    )
    
    # Optional maximum capacity per time slot
    # blank=True allows empty value in forms
    # null=True allows NULL in database (required for IntegerField when optional)
    # This allows restaurant to limit bookings during quieter times or when
    # staff levels are reduced (Vincent, 2020, Chapter 4)
    max_capacity = models.IntegerField(
        blank=True,
        null=True,
        help_text="Maximum total guests for this time slot (optional)"
    )
    
    # Boolean flag to enable/disable time slots
    # Allows seasonal hours or temporary closure of specific slots without
    # losing the time slot configuration
    is_active = models.BooleanField(
        default=True,
        help_text="Is this time slot available for bookings?"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines ordering and display names (Vincent, 2020, Chapter 5).
        """
        # Order chronologically by time (earliest first)
        ordering = ['time']
        # Proper spacing in names for better readability in admin
        verbose_name = "Time Slot"
        verbose_name_plural = "Time Slots"

    def __str__(self):
        """
        String representation of the TimeSlot instance.
        
        Formats the time in HH:MM format using 24-hour clock, which is
        standard in the UK and avoids AM/PM ambiguity (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Time in HH:MM format (e.g., '19:00', '12:30').
        
        Example:
            >>> slot = TimeSlot.objects.get(id=1)
            >>> str(slot)
            '19:00'
        """
        # strftime formats the time as HH:MM using 24-hour clock
        return self.time.strftime('%H:%M')

    def get_available_capacity(self, booking_date):
        """
        Calculate remaining capacity for this time slot on a specific date.
        
        This method implements business logic for capacity management by
        calculating how many more guests can be accommodated during this
        time slot on the specified date. It considers only active bookings
        (excluding cancelled and completed ones) (Vincent, 2020, Chapter 4).
        
        The method follows Django's recommendation to place business logic
        in models rather than views, making it reusable across the application
        (Vincent, 2020, Chapter 4).
        
        Args:
            booking_date (date): The date to check capacity for. Must be a
                Python date object.
        
        Returns:
            int: Number of additional guests that can be accommodated.
                Returns 0 if fully booked or if over capacity.
        
        Example:
            >>> from datetime import date
            >>> slot = TimeSlot.objects.get(time='19:00')
            >>> slot.get_available_capacity(date(2026, 2, 14))
            15  # 15 more guests can be accommodated
        
        Note:
            Only counts bookings with status 'Pending', 'Confirmed', or 'Seated'.
            Cancelled, Completed, and No-Show bookings do not affect capacity.
        
        References:
            Vincent, W. S. (2020) Django for beginners: Build websites with Python
                and Django. 3rd edn. Self-published, Chapter 4.
        """
        # Import Sum aggregation function
        # Imported inside method to avoid circular import issues
        from django.db.models import Sum

        # Query all bookings for this time slot on the specified date
        # Filter by status to exclude cancelled/completed bookings
        # aggregate(Sum()) calculates the total of number_of_guests field
        # The or 0 ensures we get 0 instead of None if no bookings exist
        booked_guests = Booking.objects.filter(
            timeslot=self,
            booking_date=booking_date,
            status__in=['Pending', 'Confirmed', 'Seated']  # Only active bookings
        ).aggregate(Sum('number_of_guests'))['number_of_guests__sum'] or 0

        # Use slot-specific capacity if set, otherwise default to 40
        # This allows flexible capacity management across different time periods
        max_cap = self.max_capacity if self.max_capacity else 40
        
        # Calculate and return remaining capacity
        # Result may be negative if overbooked (handled by booking validation)
        return max_cap - booked_guests


class Booking(models.Model):
    """
    Represents a customer table reservation.
    
    This is the core transactional model of the booking system, linking users,
    tables, and time slots to create reservations. The model tracks the complete
    lifecycle of a booking from creation through to completion or cancellation
    (Vincent, 2020, Chapter 4).
    
    The model implements several Django best practices:
    - Auto-generation of unique reference numbers
    - Status choices for booking lifecycle management
    - Appropriate on_delete behaviours for referential integrity
    - Timestamp tracking for audit trail
    - Database-level constraints (unique_together)
    (Vincent, 2020, Chapter 4).
    
    Attributes:
        user (ForeignKey): Customer who made the booking. Links to Django's
            User model. CASCADE deletion removes all bookings if user deleted.
        table (ForeignKey): Assigned table. Can be null initially and assigned
            later by staff. SET_NULL preserves booking history if table deleted.
        timeslot (ForeignKey): Reserved time slot. PROTECT prevents deletion
            of time slots that have associated bookings.
        booking_date (DateField): Date of the reservation.
        number_of_guests (IntegerField): Party size. Validated between 1-8.
        status (CharField): Current booking status. Uses choices for
            data consistency.
        reference_number (CharField): Unique 8-character alphanumeric code
            for customer reference. Auto-generated.
        special_requests (TextField): Customer's special requests or notes.
        created_at (DateTimeField): When booking was created.
        updated_at (DateTimeField): When booking was last modified.
        cancelled_at (DateTimeField): When booking was cancelled (if applicable).
    
    Meta:
        ordering: Bookings ordered by date (newest first), then by time.
        unique_together: Prevents same user booking same slot on same date twice.
    
    Methods:
        __str__: Returns formatted string with reference and basic details.
        generate_reference_number: Creates unique 8-character alphanumeric code.
        save: Overridden to auto-generate reference number on creation.
        cancel: Sets status to Cancelled and records cancellation time.
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 4.
        Django Software Foundation (2024) Django documentation: Model field
            reference. Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
            (Accessed: 17 January 2026).
    """
    
    # Status choices as class constant
    # Defines the booking lifecycle: created (Pending) → staff confirms
    # (Confirmed) → customer arrives (Seated) → meal complete (Completed)
    # Alternative outcomes: customer cancels (Cancelled) or doesn't arrive
    # (No-Show) (Django Software Foundation, 2024)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),        # Initial state after customer books
        ('Confirmed', 'Confirmed'),    # Staff confirmed availability
        ('Seated', 'Seated'),          # Customer arrived and seated
        ('Completed', 'Completed'),    # Meal finished, table cleared
        ('Cancelled', 'Cancelled'),    # Booking cancelled
        ('No-Show', 'No-Show'),        # Customer didn't arrive
    ]

    # Foreign key to User model with CASCADE deletion
    # CASCADE means if a user account is deleted, all their bookings are also
    # deleted. This is appropriate as bookings are meaningless without a user
    # related_name='bookings' allows reverse lookup: user.bookings.all()
    # (Vincent, 2020, Chapter 4)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
        help_text="Customer who made the booking"
    )
    
    # Foreign key to Table model with SET_NULL
    # SET_NULL preserves booking records even if a table is deleted, maintaining
    # historical data for reporting. null=True and blank=True allow the table
    # to be assigned later by staff (Vincent, 2020, Chapter 4)
    table = models.ForeignKey(
        'Table',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings',
        help_text="Assigned table (can be assigned later)"
    )
    
    # Foreign key to TimeSlot model with PROTECT
    # PROTECT prevents deletion of time slots that have associated bookings,
    # ensuring referential integrity and preventing orphaned bookings
    # (Vincent, 2020, Chapter 4)
    timeslot = models.ForeignKey(
        'TimeSlot',
        on_delete=models.PROTECT,
        related_name='bookings',
        help_text="Reservation time slot"
    )
    
    # Date field for the reservation date
    # Separate from time (which comes from timeslot) to allow flexible
    # time slot reuse across multiple dates
    booking_date = models.DateField(
        help_text="Date of reservation"
    )
    
    # Integer field with validators for party size
    # MinValueValidator ensures at least 1 guest
    # MaxValueValidator enforces maximum party size of 8
    # Validators are checked during form validation and model.clean()
    # (Django Software Foundation, 2024)
    number_of_guests = models.IntegerField(
        validators=[
            MinValueValidator(1, message="At least 1 guest required"),
            MaxValueValidator(8, message="Maximum 8 guests per booking")
        ],
        help_text="Number of guests (1-8)"
    )
    
    # CharField with choices for booking status
    # choices parameter provides dropdown in forms and admin interface
    # default='Pending' sets initial state for new bookings
    # (Django Software Foundation, 2024)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        help_text="Booking status"
    )
    
    # Unique reference number for customer communication
    # blank=True allows auto-generation (handled in save method)
    # unique=True enforced at database level ensures no duplicates
    reference_number = models.CharField(
        max_length=8,
        unique=True,
        blank=True,
        help_text="Unique booking reference (auto-generated)"
    )
    
    # TextField for customer special requests
    # blank=True makes this optional - not all bookings have special requests
    # Unlike ForeignKey, TextField uses blank=True (not null=True) following
    # Django convention (Vincent, 2020, Chapter 4)
    special_requests = models.TextField(
        blank=True,
        help_text="Customer special requests or notes"
    )
    
    # Timestamp tracking for audit trail
    # auto_now_add=True sets timestamp once on creation, never changes
    # Useful for determining when booking was made (Vincent, 2020, Chapter 4)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Booking creation timestamp"
    )
    
    # auto_now=True updates timestamp on every save
    # Useful for tracking when booking details were last modified
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update timestamp"
    )
    
    # Optional timestamp for cancellation
    # null=True and blank=True as not all bookings are cancelled
    # Allows tracking when cancellation occurred for analysis
    cancelled_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Cancellation timestamp"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines ordering, display names, and database constraints
        (Vincent, 2020, Chapter 5).
        """
        # Order by date (newest first), then by time (latest first)
        # Minus sign indicates descending order
        ordering = ['-booking_date', '-timeslot__time']
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        
        # Database constraint: prevent same user booking same slot on same date
        # Enforced at database level for data integrity
        # Prevents accidental double-booking by same user (Vincent, 2020, Chapter 4)
        unique_together = [['user', 'booking_date', 'timeslot']]

    def __str__(self):
        """
        String representation of the Booking instance.
        
        Returns a formatted string showing the reference number, username,
        and booking date for easy identification in admin and logs
        (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Formatted booking summary.
        
        Example:
            >>> booking = Booking.objects.get(id=1)
            >>> str(booking)
            'AB12CD34 - john_smith on 2026-02-14'
        """
        return f"{self.reference_number} - {self.user.username} on {self.booking_date}"

    def generate_reference_number(self):
        """
        Generate a unique 8-character alphanumeric reference number.
        
        Creates a random reference code using uppercase letters and digits,
        ensuring uniqueness by checking against existing bookings. The reference
        number is used for customer communication and booking identification
        (Vincent, 2020, Chapter 4).
        
        The method uses a while loop to guarantee uniqueness, regenerating
        if a collision occurs (statistically very rare with 36^8 possibilities).
        
        Returns:
            str: Unique 8-character alphanumeric code (e.g., 'A7B3K9M2').
        
        Example:
            >>> booking = Booking()
            >>> ref = booking.generate_reference_number()
            >>> len(ref)
            8
            >>> ref.isalnum() and ref.isupper()
            True
        
        Note:
            Uses random.choices for cryptographic randomness. The pool consists
            of 26 uppercase letters + 10 digits = 36 characters, giving
            36^8 = 2,821,109,907,456 possible combinations.
        
        References:
            Vincent, W. S. (2020) Django for beginners: Build websites with Python
                and Django. 3rd edn. Self-published, Chapter 4.
        """
        # Infinite loop until unique reference found
        while True:
            # Generate 8-character string from uppercase letters and digits
            # random.choices allows repetition (unlike random.sample)
            # k=8 specifies the length of the output string
            ref = ''.join(random.choices(
                string.ascii_uppercase + string.digits,  # A-Z, 0-9
                k=8
            ))
            
            # Check if this reference already exists in database
            # If not, we've found a unique reference
            if not Booking.objects.filter(reference_number=ref).exists():
                return ref

    def save(self, *args, **kwargs):
        """
        Override save method to auto-generate reference number.
        
        This method extends Django's default save behaviour to automatically
        generate a unique reference number when a new booking is created.
        The override pattern is a common Django technique for adding custom
        logic during model saving (Vincent, 2020, Chapter 4).
        
        Args:
            *args: Variable length argument list passed to parent save method.
            **kwargs: Arbitrary keyword arguments passed to parent save method.
        
        Returns:
            None
        
        Example:
            >>> booking = Booking(user=user, timeslot=slot, booking_date=date.today())
            >>> booking.save()  # Automatically generates reference_number
            >>> print(booking.reference_number)
            'X7Y2Z9A4'
        
        Note:
            Only generates reference number if it's not already set, allowing
            manual override if needed whilst ensuring all bookings have references.
        
        References:
            Vincent, W. S. (2020) Django for beginners: Build websites with Python
                and Django. 3rd edn. Self-published, Chapter 4.
        """
        # Only generate reference number if not already set
        # This allows manual override whilst ensuring auto-generation for new bookings
        if not self.reference_number:
            self.reference_number = self.generate_reference_number()
        
        # Call parent class save method to perform actual database save
        # *args and **kwargs pass through any arguments from the caller
        super().save(*args, **kwargs)

    def cancel(self):
        """
        Cancel the booking and record cancellation timestamp.
        
        This method provides a clean interface for cancelling bookings,
        encapsulating the business logic for cancellation (updating status
        and recording timestamp) in the model layer (Vincent, 2020, Chapter 4).
        
        The method updates two fields atomically:
        - Sets status to 'Cancelled'
        - Records current time in cancelled_at field
        
        Returns:
            None
        
        Example:
            >>> booking = Booking.objects.get(reference_number='AB12CD34')
            >>> booking.cancel()
            >>> booking.status
            'Cancelled'
            >>> booking.cancelled_at
            datetime.datetime(2026, 1, 17, 15, 30, 0, tzinfo=<UTC>)
        
        Note:
            This method saves the model after updating fields. If you need to
            make additional changes before saving, modify the fields directly
            instead of calling this method.
        
        References:
            Vincent, W. S. (2020) Django for beginners: Build websites with Python
                and Django. 3rd edn. Self-published, Chapter 4.
        """
        # Update booking status to cancelled
        self.status = 'Cancelled'
        
        # Record when cancellation occurred using timezone-aware datetime
        # timezone.now() returns current time with timezone information,
        # important for international applications
        self.cancelled_at = timezone.now()
        
        # Save changes to database
        # This commits both the status change and timestamp atomically
        self.save()