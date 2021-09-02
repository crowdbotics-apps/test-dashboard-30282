from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CountryViewSet,
    ItemViewSet,
    ItemVariantViewSet,
    ReviewViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("itemvariant", ItemVariantViewSet)
router.register("country", CountryViewSet)
router.register("review", ReviewViewSet)
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
