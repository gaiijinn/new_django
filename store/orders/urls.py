from django.urls import path
from orders.views import OrderCreateView, orders_show

app_name = 'orders'

urlpatterns = [
    path('order-create', OrderCreateView.as_view(), name='order_create'),
    path('orders_history/', orders_show.as_view(), name='orders_history'),
]
