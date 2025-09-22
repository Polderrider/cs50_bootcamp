from django.contrib import admin

# Register your models here.
from .models import Airport, Flight, Passenger


# create class to specify how flights are displayed in the admin page ie add new column headers in admin page when a flight is slected
class FlightAdmin(admin.ModelAdmin):
    list_display  = ("id", "origin", "destination", "duration")

# admin setting to manage ManyToManyField 
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin )
admin.site.register(Passenger, PassengerAdmin)


