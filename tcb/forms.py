from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class CoachCreationForm(UserCreationForm):
    class Meta:
        model = Coach
        fields = ['username', 'first_name', 'last_name', 'email']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['court',  'start_time', 'end_time', 'coach']


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['booking', 'rating', 'comment']



