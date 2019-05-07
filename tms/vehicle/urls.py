from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter(trailing_slash=False)
router.register(
    r'vehicle', views.VehicleViewSet, base_name='vehicle'
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^vehicle-brand/$', views.VehicleBrandAPIView.as_view()),
    url(r'^vehicle-model/$', views.VehicleModelAPIView.as_view()),
]
