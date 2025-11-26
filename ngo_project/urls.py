"""
URL Configuration for ngo_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views_templates import index, organizations_list, programs_list, volunteers_list, donate

urlpatterns = [
    path('', index, name='home'),
    path('organizations/', organizations_list, name='organizations'),
    path('programs/', programs_list, name='programs'),
    path('volunteers/', volunteers_list, name='volunteers'),
    path('donate/', donate, name='donate'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
