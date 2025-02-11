from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_active_rider = models.BooleanField(default=False)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return self.username


class Cycle(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance'),
    ]

    cycle_id = models.CharField(max_length=20, unique=True)
    current_location = models.JSONField(default=dict)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    lock = models.OneToOneField('Lock', on_delete=models.CASCADE, null=True, blank=True)
    last_rider = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.cycle_id} - {self.status}"


class Lock(models.Model):
    lock_id = models.CharField(max_length=20, unique=True)
    cycle = models.OneToOneField(Cycle, on_delete=models.CASCADE, related_name="lock", null=True, blank=True)
    is_locked = models.BooleanField(default=True)
    last_signal = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lock {self.lock_id} - {'Locked' if self.is_locked else 'Unlocked'}"


class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    total_time_min = models.IntegerField(null=True, blank=True)
    fare = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Ride {self.id} - {self.user.username} on {self.cycle.cycle_id}"
