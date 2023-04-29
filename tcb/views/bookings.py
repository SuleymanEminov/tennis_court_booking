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
            return redirect(reverse('tcb:bookings', args=[booking.id]))
    else:
        form = BookingForm()
    return render(request, 'tcb/booking_form.html', {'form': form})

def display_all_bookings(request):
    #  if user is logged in, show their bookings
    try:
        bookings = Booking.objects.all().filter(member=request.user)
        context = {'bookings': bookings}
    except:
        context = {}
    return render(request, 'tcb/bookings.html', context)

def display_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'tcb/display_booking.html', {'booking': booking})