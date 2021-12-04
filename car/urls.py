from django.urls import path
from car.api.viewsets import CarViewSet


urlpatterns = [
    path('cars', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'car-list'),
    path('cars/<int:pk>', CarViewSet.as_view({'get': 'retrieve', 'delete' : 'destroy'}), name = 'car-detail'),
    path('rate', CarViewSet.as_view({'post' : 'rate'}), name = 'rate-car'),
    path('popular', CarViewSet.as_view({'get' : 'popular'}), name = 'car-popular'),
]