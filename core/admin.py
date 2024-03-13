from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)

class NewUserAdmin(admin.ModelAdmin):
    NewUser_display = ('username',
                        'name',
                        'contact_no',
                        'email',
                        'age',
                        'password'
                        )

class DoctorAdmin(admin.ModelAdmin):
    DoctorDisplay=(
        'age',
        'profile_picture',
        'education',
        'address',
        'contact_no',
        'license_no',
        'password'
    )
admin.site.register(NewUser,NewUserAdmin)
admin.site.register(Doctor,DoctorAdmin)

class EventAdmin(admin.ModelAdmin):
    EventDisplay=(
        'title',
        'start_time',
        'end_time',
        'color'
    )
admin.site.register(Event,EventAdmin)

class Hospital_ImageAdmin(admin.ModelAdmin):
    HimgDisplay = (
        'user',
        'title',
        'image',
    )
admin.site.register(Hospital_Image,Hospital_ImageAdmin)

class AvailabilityAdmin(admin.ModelAdmin):
    AvailabilityDisplay=(
        'doctor',
        'day_of_week',
        'start_time',
        'end_time',
    )
admin.site.register(Availability,AvailabilityAdmin)