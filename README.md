# Django Tree Menu

A Django application that implements a tree-structured menu system with the following features:

- Menu is implemented as a template tag
- All items above the selected item are expanded
- First level of children under the selected item is also expanded
- Menu items are stored in the database
- Menu can be edited in the Django admin interface
- Active menu item is determined by the current URL
- Multiple menus can be displayed on a single page
- Menu items can use both explicit URLs and named URLs
- Only one database query is used per menu rendering

## Installation

1. Add 'tree_menu' to your INSTALLED_APPS setting:

```python
INSTALLED_APPS = [
    ...
    'tree_menu',
]
```

2. Run migrations to create the menu models:

```bash
python manage.py migrate
```

3. Include the Django admin URLs in your project's urls.py if not already included:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]
```

## Usage

### Creating Menus in Admin

1. Access the Django admin interface
2. Create a new Menu with a unique name
3. Add MenuItem objects to the menu:
   - Specify a name for each item
   - Set the URL (can be an explicit URL like '/about/' or a named URL like 'about')
   - Check 'Is Named URL' if using a named URL
   - Set a parent item for nested menu items (or leave blank for top-level items)

### Using the Template Tag

1. Load the menu tags in your template:

```html
{% load menu_tags %}
```

2. Use the draw_menu tag with the name of your menu:

```html
{% draw_menu 'main_menu' %}
```

You can have multiple menus on the same page:

```html
{% draw_menu 'main_menu' %}
{% draw_menu 'footer_menu' %}
```

## Styling

The menu is rendered as nested unordered lists (ul/li) with the following CSS classes:

- `active`: Applied to the currently active menu item
- `ancestor`: Applied to any parent of the active item
- `has-children`: Applied to any menu item that has children

You can use these classes to style the menu according to your design.

## Example

```html
{% load menu_tags %}

<div class="sidebar-menu">
    <h3>Main Navigation</h3>
    {% draw_menu 'main_menu' %}
</div>
```

## Sample Data

To populate the database with sample menu data for testing, run:

```bash
python populate_menu_data.py
```

This script will create:
1. A main menu with a 5-level deep hierarchy including:
   - Home, About, Services, Contact as top-level items
   - Multiple nested items under Services (Web Development, Mobile Development, etc.)
   - Items up to 5 levels deep (e.g., Services > Web Development > Frontend > React > React Hooks)

2. A secondary menu with:
   - Resources, Blog, FAQ, Support as top-level items
   - Items up to 5 levels deep (e.g., Resources > Documentation > API Documentation > REST API > Authentication)

The sample data includes both named URLs (like 'home', 'about') and explicit URLs (like '/services/#web').

After running the script, start the development server and navigate to the home page to see the menus in action:

```bash
python manage.py runserver
```

## Requirements

### Standard Installation
- Django
- Python 3.x

No additional libraries are required beyond Django and the Python standard library.

### Docker Installation
- Docker
- Docker Compose

## Docker Setup

This project includes Docker and Docker Compose configuration for easy deployment.

### Using Docker Compose

1. Make sure you have Docker and Docker Compose installed on your system.

2. Create a `.env` file based on the provided `.env.example`:

```bash
cp .env.example .env
```

3. Edit the `.env` file to set your desired configuration values.

4. Build and start the containers:

```bash
docker-compose up -d --build
```

5. The application will be available at http://localhost:80

6. The database migrations and initial data loading will be performed automatically during container startup.

### Docker Compose Services

The Docker Compose setup includes the following services:

- **web**: The Django application
- **db**: PostgreSQL database
- **nginx**: Nginx web server for serving the application

### Environment Variables

The following environment variables can be configured in the `.env` file:

- `DEBUG`: Set to "True" for development, "False" for production
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `SQL_ENGINE`: Database engine (default: django.db.backends.postgresql)
- `SQL_DATABASE`: Database name
- `SQL_USER`: Database user
- `SQL_PASSWORD`: Database password
- `SQL_HOST`: Database host
- `SQL_PORT`: Database port
- `DJANGO_SUPERUSER_USERNAME`: Admin username (created on startup)
- `DJANGO_SUPERUSER_EMAIL`: Admin email
- `DJANGO_SUPERUSER_PASSWORD`: Admin password
- `LOAD_INITIAL_DATA`: Set to "true" to load sample data on startup

## CI/CD

This project includes a GitHub Actions workflow for continuous integration and continuous deployment.

### Workflow Overview

The CI/CD pipeline is triggered on:
- Push to `main` or `dev` branches
- Pull requests to `main` or `dev` branches

### Jobs

The workflow includes the following jobs:

1. **Lint**: Checks code quality and style
   - Runs flake8 to check for Python syntax errors and undefined names
   - Checks code formatting with black
   - Verifies import sorting with isort

2. **Security**: Checks for security vulnerabilities
   - Scans dependencies for known security issues using safety

3. **Test**: Runs the test suite
   - Sets up a PostgreSQL database for testing
   - Runs pytest to execute the test suite
   - Only runs if lint and security checks pass

4. **Docker**: Builds and tests the Docker image
   - Builds the Docker image using the project's Dockerfile
   - Verifies that the image can be run successfully
   - Only runs if lint and security checks pass

### Running Locally

You can run the same checks locally before pushing your code:

```bash
# Install development dependencies
pip install flake8 black isort pytest pytest-django safety

# Run linting checks
flake8 .
black --check .
isort --check .

# Run security checks
safety check

# Run tests
pytest

# Build and test Docker image
docker build -t uptrader:test .
docker run --rm uptrader:test echo "Docker image built successfully"
```
