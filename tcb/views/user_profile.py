from django.contrib.auth.decorators import login_required
from ..models import User, Coach, Court, Booking, Payment, Review
from ..forms import BookingForm, PaymentForm, UserCreationForm
from django.contrib import messages
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


@login_required
def show_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'tcb/user_profile.html', context)


@login_required
def update_profile(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone_number = request.POST['phone_number']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect(reverse('tcb:user_profile'))
        
    else:
        context = {'user': user}
        return render(request, 'tcb/user_profile.html', context)