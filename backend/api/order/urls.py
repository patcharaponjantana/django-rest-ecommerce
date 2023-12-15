from django.urls import path, include
from rest_framework import routers
from api.order import views

router = routers.DefaultRouter()
router.register("item", views.OrderItemViewSet)
router.register("", views.OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
