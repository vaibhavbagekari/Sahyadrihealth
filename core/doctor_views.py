from audioop import reverse
from django.shortcuts import render, redirect
from .models import *
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
@login_required(login_url='/drsignin')
def drDashbord(request):
    # try:
        dr = Doctor.objects.get(user = request.user)
        even = dr.events.filter(user = dr)
        events_data = []
        # dr = Doctor.objects.get(id=request.user.doctors.get.id)
        for event in even:
            events_data.append({
                'title': event.title,
                'start': event.start_time.isoformat(),
                'end': event.end_time.isoformat(),
                'backgroundColor': event.color,
                'borderColor': '#27ae60'
            })

        # return JsonResponse({'status': 'success', 'events': events_data})
        return render(request,"drDashbord.html",{'events_data': events_data})
    # except Exception as e:
    #     # return JsonResponse({'status': 'error', 'message': str(e)})
    #     return render(request,"drDashbord.html")
@csrf_exempt
def updateDrData(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data','[]'))
            img = request.FILES.get("picture")
            print(data)
            ls = list(data.values())
            user = User.objects.get(username=ls[0])
            querySet = user.doctors.all()[0]
            user.first_name=ls[1]
            user.last_name=ls[2]
            user.email=ls[3]
            user.save()
            querySet.age=ls[4]
            querySet.contact_no=ls[5]
            querySet.biography=ls[6]
            querySet.category=ls[7]
            querySet.specialization=ls[8]
            querySet.experience=ls[9]
            querySet.education=ls[10]
            querySet.hospital_name=ls[11]
            querySet.license_no=ls[12]
            querySet.hospital_about=ls[13]
            if img:
                querySet.profile_picture=img
            querySet.save()
            return JsonResponse({'status': 'success'})
        else:
           return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

def drProfile(request,id):
    doctor=User.objects.filter(id=id)
    slider_img=User.objects.get(id=id).doctors.all()[0].Himgs.all()
    # if request.method == 'POST':

    # appointments = Appointment.objects.filter(doctor=doctor.doctors.all()[0])
    # context = {'doctor': doctor, 'appointments': appointments}
    # slider_img = dr.Himgs.all()
    return render(request,"drProfile.html",{'doctor':doctor,'images':slider_img})

def image_upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        img = request.FILES.get('image')
        user = request.user.doctors.all()[0]
        obj = Hospital_Image.objects.create(
            user= user,
            title = title,
            image = img
        )
        obj.save()
        return redirect("/drDashbord_setting/")
    else:
        return redirect(request.path)
def delet_img(request,id):
    Hospital_Image.objects.get(id=id).delete()
    return redirect("/drDashbord_setting/")

def image_slider(request):
    return render(request, 'drDachbord_setting.html')

def drDashbord_setting(request):
    dr_img = Doctor.objects.get(user = request.user)
    images = dr_img.Himgs.all()
    images=reversed(images)
    return render(request,'drDashbord_setting.html',{'images': images})

def availability(request):
    return render(request,'brAvailability.html')
  
@csrf_exempt  # For simplicity. You may want to use a proper CSRF token in production.
# @require_POST
def save_availability(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('availabilities','[]'))
            doctor = request.user.doctors.all()[0]
            Availability_weekly.objects.filter(doctor=doctor).delete()
            obj = Availability_weekly.objects.create(
                doctor = doctor,
                json = data
            )
            obj.save()
            return redirect(request.path)
        else:
           return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

@csrf_exempt
def save_day(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('dayEvent','[]'))
            ls1 = list(data)
            ls = list(data.values())
            doctor = request.user.doctors.all()[0]
            Availability.objects.filter(doctor=doctor).delete()
            for i in range(len(ls)):
                obj =  Availability.objects.create(
                    doctor = doctor,
                    session = ls1[i],
                    start_time = ls[i]['start'],
                    end_time = ls[i]['end']
                )
                obj.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})