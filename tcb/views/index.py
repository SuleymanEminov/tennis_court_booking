from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import User, Coach, Court, Booking, Payment, Review



def index(request):
    return render(request, 'tcb/main_page.html')

