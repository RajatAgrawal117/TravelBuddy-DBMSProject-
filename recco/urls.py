from django.urls import path, include  # Import include module
from . import views
from rest_framework.routers import DefaultRouter
from .views import TripOptionsViewSet

router = DefaultRouter()
router.register(r'trip_options', TripOptionsViewSet, basename='trip_options')

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),  # Include router-generated URLs
]
