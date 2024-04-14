from audioop import reverse
from django.shortcuts import render, redirect

# from Sahyadrihealth.core import appointment
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
        
        slots = dr.dr.all()
        slot=[]
        for i,sloti in enumerate(slots):
            slot.append(
                {
                    'date':sloti.date,
                    'start_time':sloti.start_time,
                    'end_time':sloti.end_time,
                    'Patient_name':sloti.Patient_name,
                    'Patient_contact':sloti.Patient_contact,
                    'email':sloti.email
                },
            )
        # return JsonResponse({'status': 'success', 'events': events_data})
        return render(request,"drDashbord.html",{'slots': slots})
    # except Exception as e:
    #     # return JsonResponse({'status': 'error', 'message': str(e)})
    #     return render(request,"drDashbord.html")
@csrf_exempt
def updateDrData(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data','[]'))
            img = request.FILES.get("picture")
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

@csrf_exempt
def updateGS(request):
     try:
        if request.method == 'POST':
            return JsonResponse({'status': 'success'})
        else:
           return JsonResponse({'status': 'success'})
     except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

@csrf_exempt
def getGSinsurance(request,id):
     try:
        if request.method == 'POST':
            # data=request.POST
            # print(data.get('id'))
            dr=Doctor.objects.get(id=id)
            GS = Dr_govScheme.objects.filter(doctor=dr)
            insurance=Dr_Insurance.objects.filter(doctor=dr)
            GSjson=[]
            for i in GS:
                txt={
                    'title':i.title,
                    'title_img':i.title_img.url,
                    'sub_title':i.sub_title,
                    'Document':i.Document.url,
                    'id':i.id
                }
                GSjson.append(txt)

            insurancejosn = []
            for i in insurance:
                txt={
                    'title':i.title,
                    'title_img':i.title_img.url,
                    'sub_title':i.sub_title,
                    'Document':i.Document.url,
                    'id':i.id
                }
                insurancejosn.append(txt)
            return JsonResponse({'status': 'success','GSjson':GSjson,'insurancejosn':insurancejosn})
        else:
           return JsonResponse({'status': 'success'})
     except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

@csrf_exempt
def addGS(request,id):
    try:
        if request.method == 'POST':
            dr=Doctor.objects.get(id=id)
            data = json.loads(request.POST.get('data','[]'))
            ls = list(data.values())
            
            obj = Dr_govScheme.objects.create(
                doctor=dr,
                title=ls[0],
                sub_title=ls[1],
                
            )

            obj.save()
            if request.FILES.get("title_img"):
                obj.title_img=request.FILES.get("title_img")
            if request.FILES.get("Document"):
                obj.Document=request.FILES.get("Document")
            obj.save()
            return JsonResponse({'msg': 'GS added successfully'})
        else:
           return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

@csrf_exempt
def addinsurance(request,id):
    try:
        if request.method == 'POST':
            dr=Doctor.objects.get(id=id)
            data = json.loads(request.POST.get('data','[]'))
            ls = list(data.values())
            
            obj = Dr_govScheme.objects.create(
                doctor=dr,
                title=ls[0],
                sub_title=ls[1],
                
            )

            obj.save()
            if request.FILES.get("title_img"):
                obj.title_img=request.FILES.get("title_img")
            if request.FILES.get("Document"):
                obj.Document=request.FILES.get("Document")
            obj.save()
            return JsonResponse({'msg': 'GS added successfully'})
        else:
           return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})


@csrf_exempt
def deleteGS(request,id):
    try:
        obj = Dr_govScheme.objects.get(id=id)
        obj.delete()
        return redirect("/drDashbord_setting/")
    except:
        return redirect("/drDashbord_setting/")
    

def deleteinsurance(request,id):
    try:
        obj = Dr_Insurance.objects.get(id=id)
        obj.delete()
        return redirect("/drDashbord_setting/")
    except:
        return redirect("/drDashbord_setting/")

def drProfile(request,id):
    doctor=User.objects.filter(id=id)
    slider_img=User.objects.get(id=id).doctors.all()[0].Himgs.all()
    dr = User.objects.get(id=id).doctors.all()[0]
    GS = Dr_govScheme.objects.filter(doctor=dr)
    insurance = Dr_Insurance.objects.filter(doctor=dr)
    # if request.method == 'POST':

    # appointments = Appointment.objects.filter(doctor=doctor.doctors.all()[0])
    # context = {'doctor': doctor, 'appointments': appointments}
    # slider_img = dr.Himgs.all()
    return render(request,"drProfile.html",{'doctor':doctor,'images':slider_img,'GS':GS,'insurance':insurance})

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