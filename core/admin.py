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