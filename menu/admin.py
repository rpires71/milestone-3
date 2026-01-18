"""
Django Admin Configuration for Menu Application

This module configures the Django admin interface for MenuCategory, MenuItem,
and DietaryTag models, providing tools for menu management.

References:
    Vincent, W. S. (2020) Django for beginners: Build websites with Python
        and Django. 3rd edn. Self-published, Chapter 5.
"""

from django.contrib import admin
from .models import MenuCategory, MenuItem, DietaryTag


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for MenuCategory model.
    
    Provides tools for managing menu categories and display ordering
    (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'name',
        'display_order',
        'item_count',
    ]
    
    # Fields that can be edited directly from list view
    list_editable = [
        'display_order',
    ]
    
    # Order categories by display order
    ordering = ['display_order', 'name']
    
    def item_count(self, obj):
        """
        Display the number of items in this category.
        
        Args:
            obj (MenuCategory): The category instance.
        
        Returns:
            int: Number of menu items in this category.
        """
        return obj.items.count()
    
    item_count.short_description = 'Number of Items'


@admin.register(DietaryTag)
class DietaryTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for DietaryTag model.
    
    Provides tools for managing dietary information tags with icons
    (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'icon',
        'name',
        'item_count',
    ]
    
    # Fields that can be searched
    search_fields = [
        'name',
    ]
    
    # Order tags alphabetically
    ordering = ['name']
    
    def item_count(self, obj):
        """
        Display the number of menu items with this tag.
        
        Args:
            obj (DietaryTag): The dietary tag instance.
        
        Returns:
            int: Number of menu items with this tag.
        """
        return obj.menu_items.count()
    
    item_count.short_description = 'Number of Items'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for MenuItem model.
    
    Provides comprehensive menu item management with search, filtering,
    and dietary tag management (Vincent, 2020, Chapter 5).
    """
    
    # Fields displayed in the list view
    list_display = [
        'name',
        'category',
        'price',
        'is_available',
        'get_dietary_tags',
    ]
    
    # Fields that can be edited directly from list view
    list_editable = [
        'is_available',
    ]
    
    # Filters in the right sidebar
    list_filter = [
        'category',
        'is_available',
        'dietary_info',
    ]
    
    # Fields that can be searched
    search_fields = [
        'name',
        'description',
    ]
    
    # Many-to-many fields displayed with filter widget
    filter_horizontal = [
        'dietary_info',
    ]
    
    # Fields displayed in the detail/edit view
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'category',
                'description',
            )
        }),
        ('Pricing and Availability', {
            'fields': (
                'price',
                'is_available',
            )
        }),
        ('Dietary Information', {
            'fields': (
                'dietary_info',
            )
        }),
        ('Image', {
            'fields': (
                'image',
            )
        }),
    )
    
    # Order items by category order, then alphabetically
    ordering = ['category__display_order', 'name']
    
    def get_dietary_tags(self, obj):
        """
        Display dietary tags as comma-separated list.
        
        Args:
            obj (MenuItem): The menu item instance.
        
        Returns:
            str: Comma-separated list of dietary tags with icons.
        """
        return ", ".join([str(tag) for tag in obj.dietary_info.all()])
    
    get_dietary_tags.short_description = 'Dietary Info'

