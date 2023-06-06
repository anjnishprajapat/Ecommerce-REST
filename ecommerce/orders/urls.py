from django.urls import path
from .views import create_order, get_order, update_order_status, list_orders

app_name = 'orders'

urlpatterns = [
    path('orders/', create_order, name='create_order'),
    path('orders/<int:order_id>/', get_order, name='get_order'),
    path('orders/<int:order_id>/status/', update_order_status, name='update_order_status'),
    path('orders/list/', list_orders, name='list_orders'),
]
