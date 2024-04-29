from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login



def register(request):
    if request.method == 'POST':
        # Handle registration
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            error_message = "Username already exists. Please choose a different one."
            return render(request, 'web/register.html', {'error_message': error_message})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            customer = Customer.objects.create(name=username,user=user, phone=phone, address=address)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
     
        except IntegrityError:
            error_message = "An error occurred while creating the user. Please try again later."
            return render(request, 'web/register.html', {'error_message': error_message})

    return render(request, 'web/register.html')

def user_login(request):
    if request.method == 'POST':
   
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('project_list')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'web/login.html')


def sign_out(request):
    logout(request)
    return redirect('login')
