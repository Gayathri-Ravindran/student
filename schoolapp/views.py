from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Department, Course, UserProfile, Order
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from .forms import OrderForm
def home(request):
    return render(request, 'home.html')
    # departments = Department.objects.all()
    # courses = Course.objects.all()
    # return render(request, 'order_form.html', {'departments': departments, 'courses': courses})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schoolapp:new_page')# Redirect to the new page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('schoolapp:login')


    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


@login_required  # Apply the login_required decorator to secure the view
def new_page(request):
    if request.method == 'POST':
        return redirect('schoolapp:order_form')  # Redirect to the 'order_form' view when the form is submitted
    return render(request, 'new_page.html')

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        messages.success(request, "Thank you for choosing us. Your order is confirmed.")
        # Rest of your view logic here
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})
