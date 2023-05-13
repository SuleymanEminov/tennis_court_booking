from django.urls import path
from . import views

app_name = 'tcb'
urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bookings", views.display_all_bookings, name="bookings"),
    path("bookings/<int:booking_id>", views.display_booking, name="booking"),
    path("bookings/create", views.create_booking, name="create_booking"),

    # user profile
    path("user_profile", views.show_user_profile, name="user_profile"),
    path("update_profile", views.update_profile, name="update_profile"),

    # calendar
    path("calendar", views.calendar, name="calendar"),
]