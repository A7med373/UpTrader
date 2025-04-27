from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fk_name = 'menu'
    fields = ('name', 'parent', 'url', 'is_named_url')
    raw_id_fields = ('parent',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url', 'is_named_url')
    list_filter = ('menu', 'is_named_url')
    search_fields = ('name', 'url')
    raw_id_fields = ('parent',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Limit parent choices to items from the same menu."""
        if db_field.name == "parent" and request.GET.get('menu'):
            menu_id = request.GET.get('menu')
            kwargs["queryset"] = MenuItem.objects.filter(menu_id=menu_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
