from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import Booking, Court
from ..forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def calendar(request): 
    if request.method == 'POST':
        selected_location = request.POST['location']
        # Retrieve the booked courts and times based on the selected location
        bookings = Booking.objects.filter(member=request.user, court__location=selected_location)
        all_courts = Court.objects.filter(location=selected_location)
        court_numbers = list(all_courts.values_list('court_number', flat=True))
        events = []
        for booking in bookings:
            start_time = booking.start_time
            end_time = booking.end_time
            court = booking.court
            event = {
                'title': booking.member.first_name + ' ' + booking.member.last_name,
                'start': start_time,
                'end': end_time,
                'court': court.court_number,
            }
            events.append(event)


    else:
        events = None
        all_courts = None
        court_numbers = None
    
    
    # get all court from Court model
    all_locations = Court.LOCATION
    times = ['00', '30']
    return render(request, 'tcb/calendar.html', {
        'locations': all_locations,
        'events': events,
        'times': times, 
        'all_courts': all_courts,
        'court_numbers': court_numbers,
        })


