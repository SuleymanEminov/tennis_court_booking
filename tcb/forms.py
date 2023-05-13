from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }




class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['court', 'date', 'start_time', 'end_time', 'coach']
        widgets = {
            'court': forms.Select(attrs={'class': 'form-control'}),
            'date' : DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'start_time': TimePickerInput(attrs={'class': 'form-control', 'id': 'starttime-picker', 'placeholder': 'HH:MM'}),
            'end_time': TimePickerInput(attrs={'class': 'form-control', 'id': 'endtime-picker', 'placeholder': 'HH:MM'}),
            'coach': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateUserProfile(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']




    



