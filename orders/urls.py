from django.urls import path

from orders.views import OrderCreateView

app_name = 'orders'

urlparametrs = [
    path('create/', OrderCreateView.as_view(), name='create')
]
