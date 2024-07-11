from django.urls import path
from .views import register, login_view  # Import the correct view function

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # Use the login_view
]
