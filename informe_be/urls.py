"""informe_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from account.views import register_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

# PREDEPLOY: Remove static settings before deploy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('api/user-auth/', include('account.urls')),
    path('api/project/', include('base_project.urls.project_urls')),
    path('api/item/', include('base_project.urls.item_urls')),
    path('api/indicator/', include('indicator.urls.indicator_urls')),
    path('api/evidence/', include('indicator.urls.evidence_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
