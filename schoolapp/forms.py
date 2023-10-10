from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Department, Course, Order


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Assuming you have imported the User model from django.contrib.auth.models
        fields = ['username', 'password1', 'password2']  # Include any additional fields you need for registration


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class OrderForm(forms.Form):
    username = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    phone_number = forms.CharField(max_length=10)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])
    materials = forms.ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, queryset=Order.objects.all(), label="My Checkbox")

