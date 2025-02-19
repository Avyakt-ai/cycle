from django.contrib import admin
from .models import User, Cycle, Lock, Ride
# Register your models here.

admin.site.register(User)
admin.site.register(Cycle)
admin.site.register(Lock)
admin.site.register(Ride)