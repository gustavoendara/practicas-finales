from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo de una URL
    path('', views.order_list, name='order_list'),
]