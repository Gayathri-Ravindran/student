from django.urls import path
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('new_page/', views.new_page, name='new_page'),
    path('order_form/', views.order_form, name='order_form'),


]
