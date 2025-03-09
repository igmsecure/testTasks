from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, PackageViewSet

router = DefaultRouter()
router.register(r'letters', LetterViewSet)
router.register(r'packages', PackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]