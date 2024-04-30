from django.urls import path
from orders.views import OrderCreateView, CancelTemplateView, SuccessTemplateView, OrdersListView

app_name = 'orders'

urlpatterns = [
    path('order-create', OrderCreateView.as_view(), name='order_create'),
    path('order-success', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancel', CancelTemplateView.as_view(), name='order_cancel'),
    path('orders-list', OrdersListView.as_view(), name='orders_list'),
]
