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

class Availability_weeklyAdmin(admin.ModelAdmin):
    Availability_weeklyDisplay = (
        'doctor',
        'json'
    )
admin.site.register(Availability_weekly,Availability_weeklyAdmin)

class ContactAdmin(admin.ModelAdmin):
    ConntactDisplay=(
        'fullname',
        'contact',
        'message'
    )

admin.site.register(Contact,ContactAdmin)

class AmbulanceAdmin(admin.ModelAdmin):
    AmbulanceDisplay=(
        'name',
        'name_owner',
        'about_service',
        'contact',
        'location'
    )

admin.site.register(Ambulance,AmbulanceAdmin)

class BloodStoragAdmin(admin.ModelAdmin):
    BloodStorageDisplay = (
        'name',
        'name_owner',
        'about_service',
        'contact',
        'location'
    )

admin.site.register(BloodStorage,BloodStoragAdmin)

class BookedAppoinmentAdmin(admin.ModelAdmin):
    BookedAppoinmentDisplay=(
        'doctor',
        'date',
        'start_time',
        'end_time'
    )
admin.site.register(BookedAppoinment,BookedAppoinmentAdmin)