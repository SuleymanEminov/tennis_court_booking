from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..models import User, Coach 



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("tcb:index"))
        else:
            return render(request, "tcb/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "tcb/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("tcb:index"))

# create a member object when a user registers
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = f"{first_name}{last_name}"
        email = request.POST["email"]
        # phone_number = request.POST["phone_number"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tcb/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username,
                first_name = first_name,
                last_name = last_name, 
                email = email,  
                password = password)
            user.save()
        except IntegrityError:
            return render(request, "tcb/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("tcb:index"))
    else:
        return render(request, "tcb/register.html")
