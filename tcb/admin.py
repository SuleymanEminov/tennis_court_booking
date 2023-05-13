from django.contrib import admin

# Register your models here.
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_staff', 'is_superuser')

class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_staff', 'is_superuser')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'court', 'date', 'start_time', 'end_time', 'coach', 'is_paid')
    


admin.site.register(User, UserAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Court)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment)
admin.site.register(Review)

