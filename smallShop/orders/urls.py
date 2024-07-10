from django.urls import path
from .views import add_to_cart, view_cart, checkout

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
]
