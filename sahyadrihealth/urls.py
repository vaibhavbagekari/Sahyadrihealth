"""sahyadrihealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import utils
from core import doctor_views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('about/',about,name="about"),
    path('services/',services,name="services"),
    path('findDr/',findDr,name="findDr"),
    path('',home,name="home"),
    path('contactUs/',contactUs,name='contactUs'),
    path('demo/',demo,name='demo'),
    path('demo/<id>/',delete_patient,name='delete_patient'),
    path('update-patient/<id>/',update_patient,name='update-patient'),
    path('update_patient_tem/<id>/',update_patient_tem,name='update_patient_tem'),
    path('logout/',logout_btn,name="logout_btn"),
    path('drSigUp/',drSigUp,name="drSigUp"),
    path('drDashbord/',doctor_views.drDashbord,name="drDashbord"),
    path('drsignin/',drsignin,name="drsignin"),
    path('drlogin/',drlogin,name="drlogin"),
    path('drProfile/<id>',doctor_views.drProfile,name="drProfile"),
    path('patient_signin/',patient_signin,name="patient_signin"),
    path('patient_signup',patient_signup,name="patient_signup"),
    path('patient_dashbord/',patient_dashbord,name="patient_dashbord"),
    path('goverment_scheme/',goverment_scheme,name="goverment_scheme"),
    path('search_ambulance/',search_ambulance,name="search_ambulance"),
    path('blood_storage/',blood_storage,name="blood_storage"),
    path('medical-store/',medicalStore,name="medicalStore"),
    path('save_events/<id>', save_events, name='save_events'),
    path('delete_events/<id>', delete_events, name='delete_events'),
    path('appointmentbooking/<id>', appointmentbooking, name='appointmentbooking'),
    path('update_events/<id>', update_events, name='update_events'),
    path('send_email', send_email, name='send_email'),
    path('img_upload/', doctor_views.image_upload, name='img_upload'),
    path('image_slider', doctor_views.image_slider, name='image_slider'),
    path('drDashbord_setting/', doctor_views.drDashbord_setting, name='drDashbord_setting'),
    path('updateDrData/', doctor_views.updateDrData, name='updateDrData'),
    path('delet_img/<id>', doctor_views.delet_img, name='delet_img'),
    path('updateGS/', doctor_views.updateGS, name='updateGS'),
    path('addGS/<id>', doctor_views.addGS, name='addGS'),
    path('addinsurance/<id>', doctor_views.addinsurance, name='addinsurance'),
    path('deleteGS/<id>', doctor_views.deleteGS, name='deleteGS'),
    path('deleteinsurance/<id>', doctor_views.deleteinsurance, name='deleteinsurance'),
    path('getGSinsurance/<id>', doctor_views.getGSinsurance, name='getGSinsurance'),
    # path('doctor_availability/<id>', doctor_views.doctor_availability, name='doctor_availability'),
    path('cut_event/', cut_event, name='cut_event'),
    path('availability/', doctor_views.availability, name='availability'),
    path('save_availability/', doctor_views.save_availability, name='save_availability'),
    path('save_day/', doctor_views.save_day, name='save_day'),
    path('bookAppointment/<id>', bookAppointment, name='bookAppointment'),
    path('findslots/<id>', findslots, name='findslots'),
    path('bookAppoinment/', bookAppoinment, name='bookAppoinment'),
    path('SearchAmbulance/', SearchAmbulance, name='SearchAmbulance'),
    path('SearchBloodStorage/', SearchBloodStorage, name='SearchBloodStorage'),
    path('lab_test/', lab_test, name='lab_test'),
    path('search_lab/', search_lab, name='search_lab'),
    path('healthEquipment/', healthEquipment, name='healthEquipment'),
    path('SearchhealthEquipment/', SearchhealthEquipment, name='SearchhealthEquipment'),
    path('SearchMedicalStores/', SearchMedicalStores, name='SearchMedicalStores'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

    path('developer_team/',developer_team,name='developer_team'),
    path('govenment_hospitals/',govenment_hospitals,name='govenment_hospitals'),
    path('add_gov_scheme/<scheme_id>',doctor_views.add_gov_scheme,name='add_gov_scheme'),
    path('delete_gov_scheme/<scheme_id>',doctor_views.delete_gov_scheme,name='delete_gov_scheme'),
    path('add_health_insurance/<insurance_id>',doctor_views.add_health_insurance,name='add_health_insurance'),
    path('delete_health_insurance/<insurance_id>',doctor_views.delete_health_insurance,name='delete_health_insurance')
    # path('translate/', translate_view, name='translate')

]    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()