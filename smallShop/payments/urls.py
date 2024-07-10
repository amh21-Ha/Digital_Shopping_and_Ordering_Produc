from django.urls import path
from .views import payment

urlpatterns = [
    path('payment/<int:order_id>/', payment, name='payment'),
]
