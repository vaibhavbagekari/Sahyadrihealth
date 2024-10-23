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
        'password',
        'personal_contact'
        'slotDuration'
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

class government_schemesAdmin(admin.ModelAdmin):
    government_schemesDisplay = (
        'title',
        'title_img',
        'sub_title',
        'Document',
    )
admin.site.register(Government_schemes,government_schemesAdmin)

class Dr_govSchemeAdmin(admin.ModelAdmin):
    Dr_govSchemeDisplay = (
        'doctor',
        'title',
        'title_img',
        'sub_title',
        'Document',
    )
admin.site.register(Dr_govScheme,Dr_govSchemeAdmin)

class Dr_InsuranceAdmin(admin.ModelAdmin):
    Dr_InsuranceDisplay = (
        'doctor',
        'title',
        'title_img',
        'sub_title',
        'Document'
    )
admin.site.register(Dr_Insurance,Dr_InsuranceAdmin)

class Lab_testAdmin(admin.ModelAdmin):
    Lab_testDisplay = (
        'doctor',
        'title',
        'title_img',
        'sub_title',
        'Document'
    )
admin.site.register(Lab_test,Lab_testAdmin)

class HealthEquipmentAdmin(admin.ModelAdmin):
    HealthEquipmentDisplay = (
        'title',
        'title_img',
        'sub_title'
    )
admin.site.register(HealthEquipment,HealthEquipmentAdmin)

class FeedbackquestionAdmin(admin.ModelAdmin):
    FeedbackquestionDisplay = (
        'question'
    )

admin.site.register(feedbackquestion,FeedbackquestionAdmin)

class FeedbackansAdmin(admin.ModelAdmin):
    feedbackansDisplay = (
        'questionid',
        'doctorid',
        'ans'
    )
admin.site.register(feedbackans,FeedbackansAdmin)

@admin.register(gov_scheme)
class gov_schemes(admin.ModelAdmin):
    list_display = (
        'name',
        
    )

@admin.register(health_insurance)
class health_insurances(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(gov_hopital)
class gov_hospitals(admin.ModelAdmin):
    list_display=(
        "Location",
        "Doctor_name",
        "Contact"
    )
@admin.register(MedicalStore)
class MedicalStoreAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'name_owner',
        'hospital_name',
        'about_service',
        'contact',
        'location'
    )