"""
URL configuration for UpTrader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # About subpages
    path('about/company/', TemplateView.as_view(template_name='about/company.html'), name='about_company'),
    path('about/team/', TemplateView.as_view(template_name='about/team.html'), name='about_team'),
    path('about/history/', TemplateView.as_view(template_name='about/history.html'), name='about_history'),

    # Services subpages - Level 2
    path('services/web/', TemplateView.as_view(template_name='services/web.html'), name='services_web'),
    path('services/mobile/', TemplateView.as_view(template_name='services/mobile.html'), name='services_mobile'),
    path('services/consulting/', TemplateView.as_view(template_name='services/consulting.html'), name='services_consulting'),

    # Services subpages - Level 3 (Web Development)
    path('services/web/frontend/', TemplateView.as_view(template_name='services/web/frontend.html'), name='services_web_frontend'),
    path('services/web/backend/', TemplateView.as_view(template_name='services/web/backend.html'), name='services_web_backend'),
    path('services/web/fullstack/', TemplateView.as_view(template_name='services/web/fullstack.html'), name='services_web_fullstack'),

    # Services subpages - Level 3 (Mobile Development)
    path('services/mobile/ios/', TemplateView.as_view(template_name='services/mobile/ios.html'), name='services_mobile_ios'),
    path('services/mobile/android/', TemplateView.as_view(template_name='services/mobile/android.html'), name='services_mobile_android'),

    # Services subpages - Level 4 (Frontend)
    path('services/web/frontend/react/', TemplateView.as_view(template_name='services/web/frontend/react.html'), name='services_web_frontend_react'),
    path('services/web/frontend/vue/', TemplateView.as_view(template_name='services/web/frontend/vue.html'), name='services_web_frontend_vue'),
    path('services/web/frontend/angular/', TemplateView.as_view(template_name='services/web/frontend/angular.html'), name='services_web_frontend_angular'),

    # Services subpages - Level 4 (Backend)
    path('services/web/backend/django/', TemplateView.as_view(template_name='services/web/backend/django.html'), name='services_web_backend_django'),
    path('services/web/backend/flask/', TemplateView.as_view(template_name='services/web/backend/flask.html'), name='services_web_backend_flask'),
    path('services/web/backend/node/', TemplateView.as_view(template_name='services/web/backend/node.html'), name='services_web_backend_node'),

    # Services subpages - Level 4 (iOS)
    path('services/mobile/ios/swift/', TemplateView.as_view(template_name='services/mobile/ios/swift/swift.html'), name='services_mobile_ios_swift'),
    path('services/mobile/ios/objc/', TemplateView.as_view(template_name='services/mobile/ios/objc/objc.html'), name='services_mobile_ios_objc'),

    # Services subpages - Level 4 (Android)
    path('services/mobile/android/kotlin/', TemplateView.as_view(template_name='services/mobile/android/kotlin/kotlin.html'), name='services_mobile_android_kotlin'),
    path('services/mobile/android/java/', TemplateView.as_view(template_name='services/mobile/android/java/java.html'), name='services_mobile_android_java'),

    # Services subpages - Level 5 (React)
    path('services/web/frontend/react/hooks/', TemplateView.as_view(template_name='services/web/frontend/react/hooks.html'), name='services_web_frontend_react_hooks'),
    path('services/web/frontend/react/native/', TemplateView.as_view(template_name='services/web/frontend/react/native/index.html'), name='services_web_frontend_react_native'),
    path('services/web/frontend/react/redux/', TemplateView.as_view(template_name='services/web/frontend/react/redux/index.html'), name='services_web_frontend_react_redux'),

    # Services subpages - Level 5 (Vue)
    path('services/web/frontend/vue/composition/', TemplateView.as_view(template_name='services/web/frontend/vue/composition/index.html'), name='services_web_frontend_vue_composition'),
    path('services/web/frontend/vue/vuex/', TemplateView.as_view(template_name='services/web/frontend/vue/vuex/index.html'), name='services_web_frontend_vue_vuex'),

    # Services subpages - Level 5 (Angular)
    path('services/web/frontend/angular/material/', TemplateView.as_view(template_name='services/web/frontend/angular/material/index.html'), name='services_web_frontend_angular_material'),
    path('services/web/frontend/angular/ngrx/', TemplateView.as_view(template_name='services/web/frontend/angular/ngrx/index.html'), name='services_web_frontend_angular_ngrx'),

    # Services subpages - Level 5 (Django)
    path('services/web/backend/django/rest/', TemplateView.as_view(template_name='services/web/backend/django/rest/index.html'), name='services_web_backend_django_rest'),
    path('services/web/backend/django/channels/', TemplateView.as_view(template_name='services/web/backend/django/channels/index.html'), name='services_web_backend_django_channels'),

    # Services subpages - Level 5 (Flask)
    path('services/web/backend/flask/restful/', TemplateView.as_view(template_name='services/web/backend/flask/restful/index.html'), name='services_web_backend_flask_restful'),
    path('services/web/backend/flask/sqlalchemy/', TemplateView.as_view(template_name='services/web/backend/flask/sqlalchemy/index.html'), name='services_web_backend_flask_sqlalchemy'),

    # Services subpages - Level 5 (Node.js)
    path('services/web/backend/node/express/', TemplateView.as_view(template_name='services/web/backend/node/express/index.html'), name='services_web_backend_node_express'),
    path('services/web/backend/node/nest/', TemplateView.as_view(template_name='services/web/backend/node/nest/index.html'), name='services_web_backend_node_nest'),

    # Secondary menu pages
    path('resources/', TemplateView.as_view(template_name='resources/index.html'), name='resources'),
    path('blog/', TemplateView.as_view(template_name='blog/index.html'), name='blog'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('support/', TemplateView.as_view(template_name='support.html'), name='support'),

    # Resources subpages
    path('resources/docs/', TemplateView.as_view(template_name='resources/docs/index.html'), name='resources_docs'),
    path('resources/tutorials/', TemplateView.as_view(template_name='resources/tutorials/index.html'), name='resources_tutorials'),
    path('resources/examples/', TemplateView.as_view(template_name='resources/examples/index.html'), name='resources_examples'),

    # Blog subpages
    path('blog/tech/', TemplateView.as_view(template_name='blog/tech/index.html'), name='blog_tech'),
    path('blog/news/', TemplateView.as_view(template_name='blog/news/index.html'), name='blog_news'),

    # Resources docs subpages
    path('resources/docs/api/', TemplateView.as_view(template_name='resources/docs/api/index.html'), name='resources_docs_api'),
    path('resources/docs/guides/', TemplateView.as_view(template_name='resources/docs/guides/index.html'), name='resources_docs_guides'),

    # Resources tutorials subpages
    path('resources/tutorials/beginner/', TemplateView.as_view(template_name='resources/tutorials/beginner/index.html'), name='resources_tutorials_beginner'),
    path('resources/tutorials/advanced/', TemplateView.as_view(template_name='resources/tutorials/advanced/index.html'), name='resources_tutorials_advanced'),

    # Resources examples subpages
    path('resources/examples/code/', TemplateView.as_view(template_name='resources/examples/code/index.html'), name='resources_examples_code'),
    path('resources/examples/demos/', TemplateView.as_view(template_name='resources/examples/demos/index.html'), name='resources_examples_demos'),

    # Blog tech subpages
    path('blog/tech/development/', TemplateView.as_view(template_name='blog/tech/development/index.html'), name='blog_tech_development'),
    path('blog/tech/design/', TemplateView.as_view(template_name='blog/tech/design/index.html'), name='blog_tech_design'),

    # Resources docs api subpages
    path('resources/docs/api/rest/', TemplateView.as_view(template_name='resources/docs/api/rest/index.html'), name='resources_docs_api_rest'),
    path('resources/docs/api/graphql/', TemplateView.as_view(template_name='resources/docs/api/graphql/index.html'), name='resources_docs_api_graphql'),

    # Resources docs guides subpages
    path('resources/docs/guides/installation/', TemplateView.as_view(template_name='resources/docs/guides/installation/index.html'), name='resources_docs_guides_installation'),
    path('resources/docs/guides/configuration/', TemplateView.as_view(template_name='resources/docs/guides/configuration/index.html'), name='resources_docs_guides_configuration'),

    # Resources docs api rest subpages
    path('resources/docs/api/rest/auth/', TemplateView.as_view(template_name='resources/docs/api/rest/auth/index.html'), name='resources_docs_api_rest_auth'),
    path('resources/docs/api/rest/endpoints/', TemplateView.as_view(template_name='resources/docs/api/rest/endpoints/index.html'), name='resources_docs_api_rest_endpoints'),
]
