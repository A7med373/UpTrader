from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Model representing a menu."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Menu Name')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Model representing a menu item in a tree structure."""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='Menu')
    name = models.CharField(max_length=100, verbose_name='Item Name')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        related_name='children', verbose_name='Parent Item')
    url = models.CharField(max_length=255, verbose_name='URL or URL Name')
    is_named_url = models.BooleanField(default=False, verbose_name='Is Named URL')

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['menu', 'parent__id', 'name']

    def __str__(self):
        return f"{self.menu.name} - {self.name}"

    def get_absolute_url(self):
        """Return the URL for this menu item."""
        if self.is_named_url:
            try:
                return reverse(self.url)
            except Exception:
                return '#'  # Fallback if named URL doesn't exist
        return self.url
