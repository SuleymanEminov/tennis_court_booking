from django.contrib.auth.decorators import login_required
from ..models import User, Coach, Court, Booking, Payment, Review
from ..forms import BookingForm, PaymentForm, ReviewForm
from django.contrib import messages
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.member = request.user
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect(reverse('booking_detail', args=[booking.id]))
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})