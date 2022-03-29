from django.urls import path
from .views import CompyterView, viewDetail, cart

urlpatterns = [
    path('', CompyterView, name='viewpc'),
    path('detail/<int:pk>/', viewDetail, name='detail'),
    path('cart', cart, name='cart')
]
