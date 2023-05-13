from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

    
# Member model inherits from AbstractUser and adds additional fields
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
       

# Coach model inherits from AbstractUser and adds additional fields
class Coach(User):
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    

# create models for court, booking, coach and member

# Court model has fields for name, court number, surface type and location
class Court(models.Model):
    SURFACE_TYPES = (
        ('CLAY', 'Clay'),
        ('HARD', 'Hard'),
        ('GRASS', 'Grass'),
        ('CARPET', 'Carpet'),
    )
    LOCATION = (
        ('COUNTRY_CLUB', 'Country Club'),
        ('TENNIS_CENTER', 'Tennis Center'),
        ('JCC COURTS', 'JCC Courts'),
        ('PUBLIC_COURTS', 'Public Courts'),
    )
    location = models.CharField(max_length=100, choices=LOCATION)
    surface_type = models.CharField(max_length=100, choices=SURFACE_TYPES)
    court_number = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.location} - {self.surface_type} - {self.court_number}"

# Booking model has fields for user, court, start time, end time, is paid and is cancelled

class Booking(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="members")
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name="bookings")
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, blank=True, null=True, related_name="coaches")
    date = models.DateField(default=datetime.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.court} - {self.start_time} - {self.end_time}"
    

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking} - {self.amount}"
    
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1, 6)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.booking} - {self.rating}"
    


    
