import os
import sys

import django
from django.core.management import execute_from_command_line

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UpTrader.settings")
django.setup()

from tree_menu.models import Menu, MenuItem


def create_menus():
    """Create sample menus and menu items for testing."""
    # Clear existing data
    MenuItem.objects.all().delete()
    Menu.objects.all().delete()

    print("Creating menus...")

    # Create main menu
    main_menu = Menu.objects.create(name="main_menu")

    # Create top-level items for main menu
    home = MenuItem.objects.create(menu=main_menu, name="Home", url="home", is_named_url=True)
    about = MenuItem.objects.create(menu=main_menu, name="About", url="about", is_named_url=True)
    services = MenuItem.objects.create(menu=main_menu, name="Services", url="services", is_named_url=True)
    contact = MenuItem.objects.create(menu=main_menu, name="Contact", url="contact", is_named_url=True)

    # Create second-level items
    about_company = MenuItem.objects.create(
        menu=main_menu, name="Company", url="about_company", is_named_url=True, parent=about
    )
    about_team = MenuItem.objects.create(menu=main_menu, name="Our Team", url="about_team", is_named_url=True, parent=about)
    about_history = MenuItem.objects.create(
        menu=main_menu, name="History", url="about_history", is_named_url=True, parent=about
    )

    web_dev = MenuItem.objects.create(
        menu=main_menu, name="Web Development", url="services_web", is_named_url=True, parent=services
    )
    mobile_dev = MenuItem.objects.create(
        menu=main_menu, name="Mobile Development", url="services_mobile", is_named_url=True, parent=services
    )
    consulting = MenuItem.objects.create(
        menu=main_menu, name="Consulting", url="services_consulting", is_named_url=True, parent=services
    )

    # Create third-level items
    frontend = MenuItem.objects.create(
        menu=main_menu, name="Frontend", url="services_web_frontend", is_named_url=True, parent=web_dev
    )
    backend = MenuItem.objects.create(
        menu=main_menu, name="Backend", url="services_web_backend", is_named_url=True, parent=web_dev
    )
    fullstack = MenuItem.objects.create(
        menu=main_menu, name="Full Stack", url="services_web_fullstack", is_named_url=True, parent=web_dev
    )

    ios = MenuItem.objects.create(menu=main_menu, name="iOS", url="services_mobile_ios", is_named_url=True, parent=mobile_dev)
    android = MenuItem.objects.create(
        menu=main_menu, name="Android", url="services_mobile_android", is_named_url=True, parent=mobile_dev
    )

    # Create fourth-level items
    react = MenuItem.objects.create(
        menu=main_menu, name="React", url="services_web_frontend_react", is_named_url=True, parent=frontend
    )
    vue = MenuItem.objects.create(
        menu=main_menu, name="Vue", url="services_web_frontend_vue", is_named_url=True, parent=frontend
    )
    angular = MenuItem.objects.create(
        menu=main_menu, name="Angular", url="services_web_frontend_angular", is_named_url=True, parent=frontend
    )

    django = MenuItem.objects.create(
        menu=main_menu, name="Django", url="services_web_backend_django", is_named_url=True, parent=backend
    )
    flask = MenuItem.objects.create(
        menu=main_menu, name="Flask", url="services_web_backend_flask", is_named_url=True, parent=backend
    )
    node = MenuItem.objects.create(
        menu=main_menu, name="Node.js", url="services_web_backend_node", is_named_url=True, parent=backend
    )

    swift = MenuItem.objects.create(
        menu=main_menu, name="Swift", url="services_mobile_ios_swift", is_named_url=True, parent=ios
    )
    objective_c = MenuItem.objects.create(
        menu=main_menu, name="Objective-C", url="services_mobile_ios_objc", is_named_url=True, parent=ios
    )

    kotlin = MenuItem.objects.create(
        menu=main_menu, name="Kotlin", url="services_mobile_android_kotlin", is_named_url=True, parent=android
    )
    java = MenuItem.objects.create(
        menu=main_menu, name="Java", url="services_mobile_android_java", is_named_url=True, parent=android
    )

    # Create fifth-level items
    react_hooks = MenuItem.objects.create(
        menu=main_menu, name="React Hooks", url="services_web_frontend_react_hooks", is_named_url=True, parent=react
    )
    react_native = MenuItem.objects.create(
        menu=main_menu, name="React Native", url="services_web_frontend_react_native", is_named_url=True, parent=react
    )
    redux = MenuItem.objects.create(
        menu=main_menu, name="Redux", url="services_web_frontend_react_redux", is_named_url=True, parent=react
    )

    vue_composition = MenuItem.objects.create(
        menu=main_menu, name="Composition API", url="services_web_frontend_vue_composition", is_named_url=True, parent=vue
    )
    vuex = MenuItem.objects.create(
        menu=main_menu, name="Vuex", url="services_web_frontend_vue_vuex", is_named_url=True, parent=vue
    )

    angular_material = MenuItem.objects.create(
        menu=main_menu,
        name="Angular Material",
        url="services_web_frontend_angular_material",
        is_named_url=True,
        parent=angular,
    )
    ngrx = MenuItem.objects.create(
        menu=main_menu, name="NgRx", url="services_web_frontend_angular_ngrx", is_named_url=True, parent=angular
    )

    django_rest = MenuItem.objects.create(
        menu=main_menu, name="Django REST", url="services_web_backend_django_rest", is_named_url=True, parent=django
    )
    django_channels = MenuItem.objects.create(
        menu=main_menu, name="Django Channels", url="services_web_backend_django_channels", is_named_url=True, parent=django
    )

    flask_restful = MenuItem.objects.create(
        menu=main_menu, name="Flask-RESTful", url="services_web_backend_flask_restful", is_named_url=True, parent=flask
    )
    flask_sqlalchemy = MenuItem.objects.create(
        menu=main_menu, name="Flask-SQLAlchemy", url="services_web_backend_flask_sqlalchemy", is_named_url=True, parent=flask
    )

    express = MenuItem.objects.create(
        menu=main_menu, name="Express.js", url="services_web_backend_node_express", is_named_url=True, parent=node
    )
    nest = MenuItem.objects.create(
        menu=main_menu, name="NestJS", url="services_web_backend_node_nest", is_named_url=True, parent=node
    )

    # Create secondary menu
    secondary_menu = Menu.objects.create(name="secondary_menu")

    # Create top-level items for secondary menu
    resources = MenuItem.objects.create(menu=secondary_menu, name="Resources", url="resources", is_named_url=True)
    blog = MenuItem.objects.create(menu=secondary_menu, name="Blog", url="blog", is_named_url=True)
    faq = MenuItem.objects.create(menu=secondary_menu, name="FAQ", url="faq", is_named_url=True)
    support = MenuItem.objects.create(menu=secondary_menu, name="Support", url="support", is_named_url=True)

    # Create second-level items for secondary menu
    docs = MenuItem.objects.create(
        menu=secondary_menu, name="Documentation", url="resources_docs", is_named_url=True, parent=resources
    )
    tutorials = MenuItem.objects.create(
        menu=secondary_menu, name="Tutorials", url="resources_tutorials", is_named_url=True, parent=resources
    )
    examples = MenuItem.objects.create(
        menu=secondary_menu, name="Examples", url="resources_examples", is_named_url=True, parent=resources
    )

    tech_blog = MenuItem.objects.create(menu=secondary_menu, name="Tech Blog", url="blog_tech", is_named_url=True, parent=blog)
    company_news = MenuItem.objects.create(
        menu=secondary_menu, name="Company News", url="blog_news", is_named_url=True, parent=blog
    )

    # Create third-level items for secondary menu
    api_docs = MenuItem.objects.create(
        menu=secondary_menu, name="API Documentation", url="resources_docs_api", is_named_url=True, parent=docs
    )
    user_guides = MenuItem.objects.create(
        menu=secondary_menu, name="User Guides", url="resources_docs_guides", is_named_url=True, parent=docs
    )

    beginner_tutorials = MenuItem.objects.create(
        menu=secondary_menu, name="Beginner Tutorials", url="resources_tutorials_beginner", is_named_url=True, parent=tutorials
    )
    advanced_tutorials = MenuItem.objects.create(
        menu=secondary_menu, name="Advanced Tutorials", url="resources_tutorials_advanced", is_named_url=True, parent=tutorials
    )

    code_examples = MenuItem.objects.create(
        menu=secondary_menu, name="Code Examples", url="resources_examples_code", is_named_url=True, parent=examples
    )
    demo_projects = MenuItem.objects.create(
        menu=secondary_menu, name="Demo Projects", url="resources_examples_demos", is_named_url=True, parent=examples
    )

    development_blog = MenuItem.objects.create(
        menu=secondary_menu, name="Development", url="blog_tech_development", is_named_url=True, parent=tech_blog
    )
    design_blog = MenuItem.objects.create(
        menu=secondary_menu, name="Design", url="blog_tech_design", is_named_url=True, parent=tech_blog
    )

    # Create fourth-level items for secondary menu
    rest_api_docs = MenuItem.objects.create(
        menu=secondary_menu, name="REST API", url="resources_docs_api_rest", is_named_url=True, parent=api_docs
    )
    graphql_api_docs = MenuItem.objects.create(
        menu=secondary_menu, name="GraphQL API", url="resources_docs_api_graphql", is_named_url=True, parent=api_docs
    )

    installation_guide = MenuItem.objects.create(
        menu=secondary_menu,
        name="Installation Guide",
        url="resources_docs_guides_installation",
        is_named_url=True,
        parent=user_guides,
    )
    configuration_guide = MenuItem.objects.create(
        menu=secondary_menu,
        name="Configuration Guide",
        url="resources_docs_guides_configuration",
        is_named_url=True,
        parent=user_guides,
    )

    # Create fifth-level items for secondary menu
    authentication_docs = MenuItem.objects.create(
        menu=secondary_menu, name="Authentication", url="resources_docs_api_rest_auth", is_named_url=True, parent=rest_api_docs
    )
    endpoints_docs = MenuItem.objects.create(
        menu=secondary_menu, name="Endpoints", url="resources_docs_api_rest_endpoints", is_named_url=True, parent=rest_api_docs
    )

    print("Menus created successfully!")
    print(f"Created {Menu.objects.count()} menus with {MenuItem.objects.count()} menu items.")


if __name__ == "__main__":
    create_menus()
