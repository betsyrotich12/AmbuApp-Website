from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbulanceViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'ambulances', AmbulanceViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]