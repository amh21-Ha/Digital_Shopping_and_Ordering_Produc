from django.urls import path
from .views import register, login_view, some_view  # Import the correct view function

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('some_view/', some_view, name='some_view'),
]
