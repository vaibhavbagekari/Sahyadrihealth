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
    path('drDashbord/',drDashbord,name="drDashbord"),
    path('drsignin/',drsignin,name="drsignin"),
    path('drlogin/',drlogin,name="drlogin"),
    path('drProfile/<id>',drProfile,name="drProfile"),
    path('patient_signin/',patient_signin,name="patient_signin"),
    path('patient_signup',patient_signup,name="patient_signup"),
    path('patient_dashbord/',patient_dashbord,name="patient_dashbord"),
    path('goverment_scheme/',goverment_scheme,name="goverment_scheme"),
    path('search_ambulance/',search_ambulance,name="search_ambulance"),
    path('blood_storage/',blood_storage,name="blood_storage"),
    path('save_events/<id>', save_events, name='save_events'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()