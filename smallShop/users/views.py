from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('some_view') 
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
@login_required
def some_view(request):
    return render(request, 'users/some_view.html')