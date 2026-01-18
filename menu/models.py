"""
Menu Management Models

This module defines the models for managing the restaurant menu, including
categories, dietary tags, and individual menu items.

The models implement a flexible menu system with hierarchical categorisation,
many-to-many dietary tagging, and support for pricing and availability
management (Vincent, 2020).

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published.
    Django Software Foundation (2024) Django documentation. Version 4.2.
        Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
        (Accessed: 17 January 2026).
"""

from django.db import models


class MenuCategory(models.Model):
    """
    Organises menu items into logical categories for display.
    
    This model represents menu sections such as Starters, Mains, Desserts,
    and Drinks. Categories control the display order of menu items on the
    website, allowing flexible menu organisation without requiring code
    changes (Vincent, 2020, Chapter 4).
    
    The display_order field enables custom ordering of categories, ensuring
    consistent presentation whilst allowing easy reorganisation through the
    Django admin interface (Vincent, 2020, Chapter 4).
    
    Attributes:
        name (CharField): Category name displayed to customers (e.g., "Starters",
            "Main Courses", "Desserts", "Drinks"). Limited to 100 characters
            for reasonable display length.
        display_order (IntegerField): Numerical ordering value determining
            category display sequence. Lower numbers appear first (0 appears
            before 1, etc.). Allows non-sequential numbering for easy insertion
            of new categories (e.g., 0, 10, 20, 30).
    
    Meta:
        ordering: Categories ordered primarily by display_order, then
            alphabetically by name as secondary sort.
        verbose_name: Singular name with proper spacing for admin interface.
        verbose_name_plural: Plural name correctly pluralised for admin.
    
    Methods:
        __str__: Returns the category name.
    
    Example:
        Creating categories with custom ordering:
        >>> MenuCategory.objects.create(name="Starters", display_order=10)
        >>> MenuCategory.objects.create(name="Mains", display_order=20)
        >>> MenuCategory.objects.create(name="Desserts", display_order=30)
        # Starters appear first, then Mains, then Desserts
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 4.
    """
    
    # CharField for category name with reasonable maximum length
    # max_length=100 provides sufficient space for descriptive names whilst
    # preventing unreasonably long entries (Vincent, 2020, Chapter 4)
    name = models.CharField(
        max_length=100,
        help_text="Category name (e.g., Starters, Mains)"
    )
    
    # IntegerField for manual ordering control
    # default=0 provides sensible starting value for new categories
    # Using increments of 10 (0, 10, 20, 30) leaves room to insert categories
    # between existing ones without renumbering (Vincent, 2020, Chapter 4)
    display_order = models.IntegerField(
        default=0,
        help_text="Order to display categories (0 = first)"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines default ordering and human-readable names for the Django
        admin interface (Vincent, 2020, Chapter 5).
        """
        # Primary sort by display_order (numerical), secondary sort by name (alphabetical)
        # This ensures categories appear in intended order, with alphabetical fallback
        # for categories with identical display_order values
        ordering = ['display_order', 'name']
        
        # Proper spacing in verbose names for improved readability in admin interface
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        """
        String representation of the MenuCategory instance.
        
        Returns the category name for use in Django admin, dropdowns, and
        when the model is printed or logged (Vincent, 2020, Chapter 4).
        
        Returns:
            str: The category name.
        
        Example:
            >>> category = MenuCategory.objects.get(name="Starters")
            >>> str(category)
            'Starters'
        """
        return self.name


class DietaryTag(models.Model):
    """
    Represents dietary information tags for menu items.
    
    This model stores dietary classifications such as Vegetarian, Vegan,
    Gluten-Free, Dairy-Free, etc. Tags are applied to menu items through
    a many-to-many relationship, allowing each item to have multiple dietary
    classifications and each tag to apply to multiple items
    (Django Software Foundation, 2024).
    
    The icon field supports emoji or text symbols for visual identification,
    improving accessibility and user experience by providing quick visual
    cues for dietary requirements (Vincent, 2020, Chapter 4).
    
    Attributes:
        name (CharField): Dietary tag name (e.g., "Vegetarian", "Vegan",
            "Gluten-Free"). Unique constraint ensures no duplicate tags.
            Limited to 50 characters for concise labelling.
        icon (CharField): Visual representation using emoji or text (e.g., "🌱"
            for vegetarian, "🌾" for gluten-free). Limited to 10 characters
            to accommodate emoji sequences.
    
    Meta:
        ordering: Tags ordered alphabetically by name for consistent display.
        verbose_name: Singular name with proper spacing.
        verbose_name_plural: Plural name for admin interface.
    
    Methods:
        __str__: Returns formatted string with icon and name.
    
    Example:
        Creating dietary tags:
        >>> DietaryTag.objects.create(name="Vegetarian", icon="🌱")
        >>> DietaryTag.objects.create(name="Vegan", icon="🌿")
        >>> DietaryTag.objects.create(name="Gluten-Free", icon="🌾")
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapter 4.
        Django Software Foundation (2024) Django documentation: Model field
            reference. Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
            (Accessed: 17 January 2026).
    """
    
    # CharField with unique constraint for tag name
    # unique=True enforced at database level prevents duplicate dietary tags,
    # ensuring data consistency and preventing confusion (Vincent, 2020, Chapter 4)
    # max_length=50 sufficient for standard dietary tag names
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Tag name (e.g., Vegetarian)"
    )
    
    # CharField for emoji or text icon
    # max_length=10 accommodates emoji sequences (some emoji use multiple
    # Unicode characters) whilst preventing excessively long entries
    # (Vincent, 2020, Chapter 4)
    icon = models.CharField(
        max_length=10,
        help_text="Emoji or icon (e.g., 🌱)"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines ordering and display names (Vincent, 2020, Chapter 5).
        """
        # Alphabetical ordering by name for predictable, user-friendly display
        ordering = ['name']
        
        # Proper spacing in names for admin interface readability
        verbose_name = "Dietary Tag"
        verbose_name_plural = "Dietary Tags"

    def __str__(self):
        """
        String representation of the DietaryTag instance.
        
        Returns a formatted string combining the icon and name, providing
        visual identification alongside text label for improved usability
        (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Formatted string with icon and name.
        
        Example:
            >>> tag = DietaryTag.objects.get(name="Vegetarian")
            >>> str(tag)
            '🌱 Vegetarian'
        """
        # Combine icon and name with space separator for readable display
        return f"{self.icon} {self.name}"


class MenuItem(models.Model):
    """
    Represents individual dishes offered by the restaurant.
    
    This model stores complete information about menu items including name,
    description, pricing, categorisation, dietary information, and availability
    status. It serves as the central model for menu management and customer
    menu display (Vincent, 2020, Chapter 4).
    
    The model implements two types of relationships:
    - ForeignKey to MenuCategory (many-to-one): Each item belongs to exactly
      one category, but categories can contain multiple items.
    - ManyToManyField to DietaryTag: Items can have multiple dietary tags,
      and tags can apply to multiple items (Django Software Foundation, 2024).
    
    The ImageField allows uploading dish photographs, enhancing menu presentation
    and customer decision-making. Images are stored in the 'menu_items/' directory
    within MEDIA_ROOT (Vincent, 2020, Chapter 10).
    
    Attributes:
        name (CharField): Dish name displayed to customers (e.g., "Grilled
            Sea Bass", "Chocolate Tart"). Limited to 200 characters.
        category (ForeignKey): Link to MenuCategory. CASCADE deletion removes
            items when their category is deleted, maintaining referential integrity.
        description (TextField): Detailed dish description including ingredients,
            preparation method, or serving suggestions. Unlimited length for
            comprehensive descriptions.
        price (DecimalField): Item price in British Pounds. Uses Decimal type
            for precise monetary calculations, avoiding floating-point errors.
            Format: 999.99 (max_digits=5, decimal_places=2).
        dietary_info (ManyToManyField): Links to DietaryTag models. blank=True
            allows items without dietary tags (Django Software Foundation, 2024).
        is_available (BooleanField): Current availability status. Allows
            temporary removal from display without deletion, preserving
            historical data and enabling seasonal menus.
        image (ImageField): Optional dish photograph. Images uploaded to
            'menu_items/' subdirectory. blank=True and null=True make this
            field optional (Vincent, 2020, Chapter 10).
    
    Meta:
        ordering: Items ordered by category's display_order, then alphabetically
            by name within each category.
        verbose_name: Singular name with proper spacing.
        verbose_name_plural: Plural name for admin interface.
    
    Methods:
        __str__: Returns formatted string with name and price.
    
    Example:
        Creating a menu item:
        >>> category = MenuCategory.objects.get(name="Mains")
        >>> item = MenuItem.objects.create(
        ...     name="Grilled Sea Bass",
        ...     category=category,
        ...     description="Fresh sea bass with seasonal vegetables",
        ...     price=18.50
        ... )
        >>> veg_tag = DietaryTag.objects.get(name="Gluten-Free")
        >>> item.dietary_info.add(veg_tag)
    
    References:
        Vincent, W. S. (2020) Django for beginners: Build websites with Python
            and Django. 3rd edn. Self-published, Chapters 4, 10.
        Django Software Foundation (2024) Django documentation: Model field
            reference. Available at: https://docs.djangoproject.com/en/4.2/ref/models/fields/
            (Accessed: 17 January 2026).
    """
    
    # CharField for dish name
    # max_length=200 accommodates descriptive dish names whilst preventing
    # unreasonably long entries that would disrupt menu layout (Vincent, 2020, Chapter 4)
    name = models.CharField(
        max_length=200,
        help_text="Dish name"
    )
    
    # ForeignKey to MenuCategory establishes many-to-one relationship
    # on_delete=models.CASCADE removes menu items when their category is deleted,
    # preventing orphaned items without categories (Vincent, 2020, Chapter 4)
    # related_name='items' enables reverse lookup: category.items.all()
    category = models.ForeignKey(
        'MenuCategory',
        on_delete=models.CASCADE,
        related_name='items',
        help_text="Menu category (Starters, Mains, etc.)"
    )
    
    # TextField for unlimited-length description
    # Allows comprehensive dish descriptions including ingredients, preparation,
    # serving suggestions, or allergen information (Vincent, 2020, Chapter 4)
    description = models.TextField(
        help_text="Dish description"
    )
    
    # DecimalField for monetary values
    # Uses Decimal type instead of Float to avoid floating-point arithmetic
    # errors in financial calculations (Vincent, 2020, Chapter 4)
    # max_digits=5 allows prices up to 999.99
    # decimal_places=2 provides standard currency precision (pence)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Price in GBP (e.g., 12.50)"
    )
    
    # ManyToManyField creates many-to-many relationship with DietaryTag
    # Each menu item can have multiple dietary tags (Vegetarian AND Gluten-Free)
    # Each tag can apply to multiple items
    # blank=True allows items without any dietary tags
    # Django automatically creates junction table: menu_menuitem_dietary_info
    # (Django Software Foundation, 2024)
    dietary_info = models.ManyToManyField(
        'DietaryTag',
        blank=True,
        related_name='menu_items',
        help_text="Dietary tags (Vegetarian, Vegan, etc.)"
    )
    
    # BooleanField for availability status
    # default=True means new items are available unless explicitly set otherwise
    # Allows "soft deletion" - items can be made unavailable without losing
    # historical data, supporting seasonal menus and temporary unavailability
    # (Vincent, 2020, Chapter 4)
    is_available = models.BooleanField(
        default=True,
        help_text="Is this item currently available?"
    )
    
    # ImageField for dish photographs
    # upload_to='menu_items/' specifies subdirectory within MEDIA_ROOT
    # blank=True allows empty value in forms (optional field)
    # null=True allows NULL in database (required for optional ImageField)
    # Requires Pillow library for image processing (Vincent, 2020, Chapter 10)
    image = models.ImageField(
        upload_to='menu_items/',
        blank=True,
        null=True,
        help_text="Optional dish photo"
    )

    class Meta:
        """
        Model metadata configuration.
        
        Defines default ordering and display names (Vincent, 2020, Chapter 5).
        """
        # Complex ordering: first by category's display_order (via relationship),
        # then alphabetically by item name within each category
        # Double underscore notation (__) traverses relationships in queries
        # This groups items by category in intended order (Vincent, 2020, Chapter 4)
        ordering = ['category__display_order', 'name']
        
        # Proper spacing in names for admin interface
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        """
        String representation of the MenuItem instance.
        
        Returns a formatted string showing the dish name and price in British
        Pounds, providing clear identification in admin interface, logs, and
        when the model is printed (Vincent, 2020, Chapter 4).
        
        Returns:
            str: Formatted string with name and price.
        
        Example:
            >>> item = MenuItem.objects.get(name="Grilled Sea Bass")
            >>> str(item)
            'Grilled Sea Bass - £18.50'
        
        Note:
            Price displays with pound sign (£) for British currency.
            DecimalField automatically formats to 2 decimal places.
        """
        # Format with British pound sign for currency display
        # DecimalField ensures consistent 2 decimal place formatting
        return f"{self.name} - £{self.price}"
    
