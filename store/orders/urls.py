from django.urls import path
from orders.views import orderCreateView

app_name = 'orders'

urlpatterns = [
    path('order-create', orderCreateView.as_view(), name='order-create'),
]
