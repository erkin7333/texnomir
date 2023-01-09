from django.urls import path, include
from .views import LeadViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')

urlpatterns = [
    path('', include(router.urls))
]