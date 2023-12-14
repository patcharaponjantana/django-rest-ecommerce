from django.urls import include, path
from rest_framework import routers
from api.product import views

router = routers.DefaultRouter()
router.register("category", views.ProductCategoryViewSet)
router.register("", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]