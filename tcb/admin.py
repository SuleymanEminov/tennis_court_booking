from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Court)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)

