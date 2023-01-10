from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClentViewSet


router = DefaultRouter()
router.register('clients', ClentViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls))
]
