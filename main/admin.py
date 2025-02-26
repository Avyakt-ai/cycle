from django.contrib import admin
from .models import UserProfile, Cycle, Lock, Ride
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Cycle)
admin.site.register(Lock)
admin.site.register(Ride)