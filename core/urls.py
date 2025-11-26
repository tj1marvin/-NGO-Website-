from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'programs', views.ProgramViewSet)
router.register(r'volunteers', views.VolunteerViewSet)
router.register(r'donations', views.DonationViewSet)
router.register(r'impacts', views.ImpactViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
