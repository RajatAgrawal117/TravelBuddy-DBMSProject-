from django.contrib import admin

# Register your models here.
from .models import Destination, Activity, Accommodation

admin.site.register(Destination)
admin.site.register(Accommodation)
admin.site.register(Activity)

