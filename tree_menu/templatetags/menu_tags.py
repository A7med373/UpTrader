from django import template
from django.utils.safestring import mark_safe

from tree_menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Template tag to draw a tree menu.

    Usage: {% draw_menu 'main_menu' %}

    Requirements:
    1. All items above the selected item are expanded
    2. First level of children under the selected item is also expanded
    3. Active item is determined by the current URL
    4. Only one database query per menu
    """
    request = context["request"]
    current_path = request.path

    # Get the menu and all its items in a single query
    try:
        menu = Menu.objects.prefetch_related("items").get(name=menu_name)
    except Menu.DoesNotExist:
        return mark_safe(f"<!-- Menu '{menu_name}' does not exist -->")

    # Get all menu items for this menu
    menu_items = menu.items.select_related("parent").all()

    # Create a dictionary of items by their IDs for easy lookup
    items_dict = {item.id: item for item in menu_items}

    # Create a dictionary of children for each parent
    children_dict = {}
    for item in menu_items:
        parent_id = item.parent_id if item.parent_id else 0
        if parent_id not in children_dict:
            children_dict[parent_id] = []
        children_dict[parent_id].append(item)

    # Find the active item
    active_item_id = None
    active_item_ancestors = []

    # First, try to find an exact URL match
    for item in menu_items:
        item_url = item.get_absolute_url()
        # Handle exact match for the full URL
        if item_url == current_path:
            active_item_id = item.id
            break
        # Handle URLs with fragment identifiers for exact path match
        elif "#" in item_url:
            url_path = item_url.split("#")[0]
            # If the URL path is empty or just a slash, use the current path
            if not url_path or url_path == "/":
                url_path = current_path
            # Check if the current path matches the URL path
            if url_path == current_path:
                active_item_id = item.id
                break

    # If no exact match, find the closest match (for nested URLs)
    if active_item_id is None:
        max_match_length = 0
        for item in menu_items:
            item_url = item.get_absolute_url()

            # Handle URLs with fragment identifiers
            if "#" in item_url:
                url_path = item_url.split("#")[0]
                # If the URL path is empty or just a slash, use the current path
                if not url_path or url_path == "/":
                    url_path = current_path

                # Check if the current path matches or starts with the URL path
                if url_path == current_path or (
                    current_path.startswith(url_path) and len(url_path) > max_match_length and url_path != "/"
                ):
                    # For exact matches, set as active and break
                    if url_path == current_path:
                        active_item_id = item.id
                        break
                    # For partial matches, keep track of the longest match
                    elif len(url_path) > max_match_length:
                        max_match_length = len(url_path)
                        active_item_id = item.id
            # Regular URL matching for nested paths
            elif current_path.startswith(item_url) and len(item_url) > max_match_length and item_url != "/":
                max_match_length = len(item_url)
                active_item_id = item.id

    # Build the list of ancestors for the active item
    if active_item_id:
        current_id = active_item_id
        while current_id:
            active_item_ancestors.append(current_id)
            parent_id = items_dict[current_id].parent_id
            current_id = parent_id

    # Render the menu
    result = _render_menu_level(0, children_dict, items_dict, active_item_id, active_item_ancestors)
    return mark_safe(result)


def _render_menu_level(parent_id, children_dict, items_dict, active_item_id, active_item_ancestors):
    """
    Recursively render a level of the menu.

    Args:
        parent_id: ID of the parent item (0 for root level)
        children_dict: Dictionary mapping parent IDs to lists of child items
        items_dict: Dictionary mapping item IDs to MenuItem objects
        active_item_id: ID of the currently active item
        active_item_ancestors: List of IDs of ancestors of the active item

    Returns:
        HTML string for this level of the menu
    """
    if parent_id not in children_dict:
        return ""

    result = "<ul>"
    for item in children_dict[parent_id]:
        is_active = item.id == active_item_id
        is_ancestor = item.id in active_item_ancestors
        has_children = item.id in children_dict

        # Determine if this item should be expanded
        expand_children = is_active or is_ancestor

        # Build the item's HTML
        css_classes = []
        if is_active:
            css_classes.append("active")
        if is_ancestor:
            css_classes.append("ancestor")
        if has_children:
            css_classes.append("has-children")

        class_attr = f' class="{" ".join(css_classes)}"' if css_classes else ""
        result += f'<li{class_attr}><a href="{item.get_absolute_url()}">{item.name}</a>'

        # Render children if this item should be expanded
        if has_children and expand_children:
            result += _render_menu_level(item.id, children_dict, items_dict, active_item_id, active_item_ancestors)

        result += "</li>"

    result += "</ul>"
    return result
