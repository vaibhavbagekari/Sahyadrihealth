from operator import ne
from os import name
from urllib import request
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.shortcuts import redirect, render
import pandas as pd
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.http import require_GET
from datetime import timedelta
import time
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
import datetime
from .utils import send_email_to_client,send_email_to_dr,send_email_to_admin
from datetime import time as dt_time

def creatPatient(request):
    if request.method == "POST":
        data=request.POST
        fullName = data.get('fullName')
        contactNumber = data.get('contactNumber')
        email = data.get('email')
        username=email
        age = data.get('age')
        password = data.get('password')
        user_check = User.objects.filter(username = username)
        
        if user_check.exists():
            msg="username is allredy exist"
            messages.add_message(request, messages.INFO, msg)
            return redirect(request.path)
        else:
            main_user=User.objects.create(
                username=email,
                email=email
            )
            main_user.set_password(password)
            main_user.save()

            user=NewUser.objects.create(
                user=main_user,
                name=fullName,
                contact_no=contactNumber,
                age=age
            )
            
            user.save()
            user = authenticate(username=username,password=password)
            login(request,user)
            msg="successful"
            messages.add_message(request, messages.INFO, msg)
            return redirect('/patient_dashbord/')

def patient_signup(request):
    if request.method == "POST":
        return creatPatient(request)
    else:
        return render(request,"patient_signup.html")
    
@ensure_csrf_cookie
@csrf_protect   
def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)

        try:
            patient_data=User.objects.get(username=username).patients.all()
        except User.DoesNotExist:
            messages.error(request,'Invalid credentials')
            return  redirect(request.path)
        
        if not User.objects.filter(username = username).exists():
            messages.add_message(request, messages.INFO, 'Invalid username')
            return redirect(request.path)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect(request.path)
        
        elif not patient_data:
            messages.error(request,'Invalid credentials')
            return  redirect(request.path)
        else:
            main_data=User.objects.get(username=user)
            login(request,user)
            messages.add_message(request,messages.INFO,'login Successful')
            return render(request,"patient_dashbord.html",{'patient_data':patient_data,'main_data':main_data})
            # return redirect(request.path)

def patient_signin(request):
    if request.method == 'POST':
        return signin(request)
    else:
        return render(request,"patient_signin.html")
    
@login_required(login_url='/patient_signin')
def patient_dashbord(request):
    if request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"patient_dashbord.html",{'data':data,'m':m})
        else:
            return render(request,"patient_dashbord.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,'patient_dashbord.html')

def logout_btn(request):
    logout(request)
    return redirect('/home/')

def check_form(request):
        data=request.POST
        if data.get('check')=='SignUp':
            return creatPatient(request)
        else:
            return signin(request)

def delete_patient(request,id):
    querySet = Patient.objects.get(id=id)
    querySet.delete()
    return redirect('/demo/')

def update_patient(request,id):
    if request.method == "POST":
        data=request.POST
        querySet = Patient.objects.get(id=id)
        querySet.name = data.get('fullName')
        querySet.contact_no = data.get('contactNumber')
        querySet.email = data.get('email')
        querySet.age = data.get('age')
        querySet.password = data.get('password')
        querySet.save()
        return redirect('/demo/')

def update_patient_tem(request,id):
    queryset = Patient.objects.get(id=id)
    context = {'Patient':queryset}
    return render(request,"update-patient.html",context)   
 
def get_locations():
    list = []
    data = Doctor.objects.all()
    for i in data:
        list.append(i.address)
    return list

def cut_event(request):
    return redirect(request.path)

def home(request):
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"index.html",{'data':data,'m':m})
        else:
            return render(request,"index.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"index.html")

def about(request):
     if request.method == 'POST':
        return check_form(request)
     elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        ad=request.GET.get('location')
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"about.html",{'data':data,'m':m})
        else:
            return render(request,"about.html",{'data':data,'ad':ad,'count':count})
     else:
        return render(request,"about.html")

def services(request):
     if request.method == 'POST':
        return check_form(request)
     elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"services.html",{'data':data,'m':m})
        else:
            return render(request,"services.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
     else:
         return render(request,"services.html")

def findDr(request):
     if request.method == 'POST':
        return check_form(request)
     elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"findDrNearYou.html",{'data':data,'m':m})
        else:
            return render(request,"findDrNearYou.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
        
     elif request.GET.get('Flocation'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('Flocation'),category__icontains=request.GET.get('Fcategory'))
        count=len(data)
        ad=request.GET.get('Flocation')
        if not data.exists():
           m="doctor not found"
           return render(request,"findDrNearYou.html",{'Fdata':data,'Fm':m})
        else:
            l=get_locations()
            return render(request,"findDrNearYou.html",{'Fdata':data,'Fcount':count,'Fad':ad,'Flocations':l})
         
     else:
        return render(request,"findDrNearYou.html")

def contactUs(request):
     if request.method == 'POST':
        if request.POST.get('check')=='contactform':
            fullname = request.POST.get('fullName')
            contact = request.POST.get('contact')
            message= request.POST.get('message')
            obj = Contact.objects.create(
                fullname=fullname,
                contact=contact,
                message=message
            )
            obj.save()
            messages.add_message(request, messages.INFO, "Message has been Send successfully, Thank You !")
            return redirect(request.path)
        else:
            return check_form(request)
     elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"contactUs.html",{'data':data,'m':m})
        else:
            return render(request,"contactUs.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
     else:
        return render(request,"contactUs.html")

def goverment_scheme(request):
    GS=Government_schemes.objects.all()
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        
        if not data.exists():
           m="doctor not found"
           return render(request,"goverment_scheme.html",{'data':data,'m':m,'GS':GS})
        else:
            return render(request,"goverment_scheme.html",{'data':data,'count':count,'ad':ad,'locations':get_locations(),'GS':GS})
    else:
        return render(request,"goverment_scheme.html",{'GS':GS})
    
def search_ambulance(request):
    if request.GET.get('locationOfAmbulance'):
        l=request.GET.get('locationOfAmbulance')
    elif request.GET.get('locationInput'):
        loc=request.GET.get('locationInput')
        return render(request,"search_ambulance.html")

    elif request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"search_ambulance.html",{'data':data,'m':m})
        else:
            return render(request,"search_ambulance.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"search_ambulance.html")

def blood_storage(request):
    
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"blood_storage.html",{'data':data,'m':m})
        else:
            return render(request,"blood_storage.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"blood_storage.html")

def demo(request):
    return render(request,"demo.html")

def medicalStore(request):
    return render(request,"medicalStore.html")

@ensure_csrf_cookie
@csrf_protect 
def drSigUp(request):
    try:
        if request.method == "POST":
            data = request.POST
            first_name = data.get('FName')
            last_name = data.get('LName')
            # age = data.get('age')
            email=data.get('email')
            profile_picture = request.FILES.get('Pfile')
            education = data.get('education')
            address = data.get('address')
            contact_no = data.get('contact_no')
            personal_contact = data.get('personal_contact')
            # license_no = data.get('licenseNumber')
            password=data.get('password')
            username=data.get('email')
            specialization=data.get('specialization')
            catagory = data.get('categorySelect')
            
            obj = User.objects.filter(username=username)
            if obj.exists():
                msg="username is allredy exist"
                messages.add_message(request, messages.INFO, msg)

            else:
                main_user = User.objects.create(
                    first_name=first_name,
                    username=username,
                    last_name=last_name,
                    email=email,
                )
                main_user.set_password(password)
                main_user.save()
                doctor = Doctor.objects.create(
                    user=main_user,
                    # age=age,
                    profile_picture=profile_picture,
                    education=education,
                    address=address,
                    contact_no=contact_no,
                    personal_contact=personal_contact,
                    # license_no=license_no,
                    specialization=specialization,
                    category=catagory
                )
                doctor.save()
                drData={'email':main_user.email,'name':main_user.first_name+" "+main_user.last_name,'username':username,'email':email}
                msg="Account created Successfuly"
                messages.add_message(request, messages.INFO, msg)
                return render(request,"drsignin.html")
        return render(request,"drSigUp.html")
    except:
        messages.error(request,'Someting went Wroung')
        return render(request,"drSigUp.html")


@ensure_csrf_cookie
@csrf_protect
def drlogin(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
       
        if not User.objects.filter(username = username).exists():
            messages.add_message(request, messages.INFO, 'Invalid username')
            return render(request,"drsignin.html")
        doctor = authenticate(username=username,password=password)
        obj = User.objects.get(username=username).doctors.all()
        
        if doctor is None:
            messages.error(request,'Invalid Password')
            return render(request,"drsignin.html")
        elif not obj:
            messages.error(request,'Invalid credentials')
            return render(request,"drsignin.html")
        else:
            # doctor_data = User.objects.get(username=doctor).doctors.all()
            login(request,doctor)
            messages.add_message(request,messages.INFO,'login Successful')
            return redirect('/drDashbord/')
        
def drsignin(request):
    return render(request,"drsignin.html")

@csrf_exempt  # For simplicity. You may want to use a proper CSRF token in production.
@require_POST
def save_events(request,id):
    try:

     if request.method == 'POST':
            data = json.loads(request.POST.get('events', '[]'))
            dr = Doctor.objects.get(id=id)
            for event_data in data:
                event = dr.events.create(
                    user=dr,
                    title=event_data.get('title', ''),
                    start_time=event_data.get('start'),
                    end_time=event_data.get('end'),
                    color=event_data.get('backgroundColor', '#2ecc71')
                )
                event.save()
            
            return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
@csrf_exempt  # For simplicity. You may want to use a proper CSRF token in production.
@require_POST
def delete_events(request,id):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('ed', '[]'))
            dr = Doctor.objects.get(id=id)
            k=dr.events.filter(start_time=data['start'])
            k.delete()
            
            return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
@login_required(login_url='/patient_signin')
def appointmentbooking(request,id):
    doctor=User.objects.filter(id=id)
    for i in doctor:
        u = i.username

    dr = Doctor.objects.get(user = u)
    even = dr.events.all()
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
    return render(request,"AppointmentBooking.html",{'events_data':events_data,'doctor':doctor})

@csrf_exempt  # For simplicity. You may want to use a proper CSRF token in production.
@require_POST
def update_events(request,id):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('events', '[]'))
            dr = User.objects.get(id=id)
            d=Doctor.objects.get(user = dr.username)
            k=d.events.get(start_time=data['start'],end_time=data['end'])
            k.title=data['title']
            k.color=data['backgroundColor']
            k.patient_booked=data['patient_booked']
            k.time_of_booking=datetime.datetime.now()
           
            us = User.objects.get(username=data['patient_booked'])
            p=NewUser.objects.get(user = us.username)
            send_email_to_client(k,dr,p)
            k.save()
            return JsonResponse({'status': 'success'})
    except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
def send_email(request):
    send_email_to_client()
    return redirect("/")

def bookAppointment(request,id):
    return render(request,"bookAppointment.html")

def daterange(date1, date2):
    import datetime
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    return [date1 + datetime.timedelta(days=x) for x in range((date2-date1).days +1)]

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def divide_time_slots(start_time, end_time, slot_duration):
    slots = {}
    start_time_str = start_time.strftime("%H:%M")
    end_time_str = end_time.strftime("%H:%M")
    # Convert string times to datetime objects
    start = datetime.strptime(start_time_str, "%H:%M")
    end = datetime.strptime(end_time_str, "%H:%M")
    
    current_slot_start = start
    while current_slot_start < end:
        current_slot_end = current_slot_start + timedelta(minutes=slot_duration)
        
        if current_slot_end > end:
            current_slot_end = end
        

        slots[current_slot_start.strftime("%H:%M") + "-" + current_slot_end.strftime("%H:%M")] = {
            "start": current_slot_start.strftime("%H:%M"),
            "end": current_slot_end.strftime("%H:%M")
        }
        
        current_slot_start = current_slot_end
    return slots

def divide_time_slots_current_date(start_time, end_time, slot_duration,threshold_time,d):
    slots = {}
    start_time_str = start_time.strftime("%H:%M")
    end_time_str = end_time.strftime("%H:%M")
    # Convert string times to datetime objects
    start = datetime.strptime(start_time_str, "%H:%M")
    end = datetime.strptime(end_time_str, "%H:%M")
    
    current_slot_start = start
    while current_slot_start < end:
        current_slot_end = current_slot_start + timedelta(minutes=slot_duration)
        
        if current_slot_end > end:
            current_slot_end = end
        # print("date :",d,"cuuent end time:",current_slot_end.time(),"  ","threshold time ",threshold_time ," status : ",current_slot_end.time()>threshold_time)

       
        if (current_slot_end.time()>threshold_time):
            slots[current_slot_start.strftime("%H:%M") + "-" + current_slot_end.strftime("%H:%M")] = {
                "start": current_slot_start.strftime("%H:%M"),
                "end": current_slot_end.strftime("%H:%M")
            }
        
        current_slot_start = current_slot_end
    return slots

from datetime import datetime, time as dt_time, timedelta
from datetime import date
def getSlots(id,day,d):
    dr = Doctor.objects.get(id=id)
    data = Availability_weekly.objects.get(doctor=dr)
    m=data.json
    slot_duration=dr.slotDuration
    ls=("Morning","Afternoon","Evening")
    jn=[]
    current_date = date.today()
    current_time_seconds = time.time()
    current_time_struct = time.localtime(current_time_seconds)
    hour = current_time_struct.tm_hour
    minute = current_time_struct.tm_min
    second = current_time_struct.tm_sec
    # Create a datetime.time object
    datetime_time_obj = dt_time(hour, minute, second)
    dummy_date = datetime(1900, 1, 1)  # You can use any date here, it won't matter for time calculation
    combined_datetime = datetime.combine(dummy_date, datetime_time_obj)
    threshold_time=(combined_datetime+timedelta(hours=7)).time()
    if current_date==d.date():
        for i in ls:
            if m[day][i.lower()]:
                h=Availability.objects.filter(doctor=dr,session=i)
                j={
                    "session":i,
                    "slots":divide_time_slots_current_date(h[0].start_time,h[0].end_time,slot_duration,threshold_time,d)
                }
                jn.append(j)
    else:
        for i in ls:
            if m[day][i.lower()]:
                h=Availability.objects.filter(doctor=dr,session=i)
                j={
                    "session":i,
                    "slots":divide_time_slots(h[0].start_time,h[0].end_time,slot_duration)
                }
                jn.append(j)
    return jn

def convert_time_format(time_string):
    date, time_range = time_string.split(' ')
    start_time, end_time = time_range.split('-')
    formatted_start_time = start_time[:-3]  # Remove the last 3 characters (":00")
    formatted_end_time = end_time[:-3]  # Remove the last 3 characters (":00")
    return f"{date} {formatted_start_time}-{formatted_end_time}"

@csrf_exempt
def findslots(request,id):
    try:
        if request.method == 'POST':
            date = json.loads(request.POST.get('date', '[]'))
            ls=list(date.values())
            date_list = daterange(ls[0].split('T')[0], ls[1].split('T')[0])
            jn=[]

            for i in date_list:
                d=pd.Timestamp(i)
                j={
                    "date":i.strftime('%Y-%m-%d'),
                    "day":d.day_name(),
                    "slots":getSlots(id,d.day_name(),i)
                }
                jn.append(j)
            dr = Doctor.objects.get(id=id)
            data = BookedAppoinment.objects.filter(doctor=dr)
            bookedsots = []
            for i in data :
                slot = str(i.date) +" "+ str(i.start_time)+"-"+str(i.end_time)
                bookedsots.append(convert_time_format(slot))
            return JsonResponse({'status': 'success',"context":jn,"bookedsots":bookedsots})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

@csrf_exempt
def bookAppoinment(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', '[]'))
            ls=list(data.values())
            id=ls[0]
            id=int(id)
            dr = User.objects.get(id=id)
            d=Doctor.objects.get(user = dr.username)
            date=ls[1]
            stime=ls[2]
            etime=ls[3]
            patient_name=ls[4]
            contact_no=ls[5]
            email=ls[6]
            obj = BookedAppoinment.objects.create(
                doctor=d,
                date=date,
                start_time=stime,
                end_time=etime,
                Patient_name=patient_name,
                Patient_contact=contact_no,
                email=email
            )
            patientData = {'email':email,'name':patient_name,'contact':contact_no}
            drData={'email':dr.email,'name':dr.first_name+" "+dr.last_name,'hospital_name':d.hospital_name}
            obj.save()
            slotData={'date':date,'stime':stime,'etime':etime,'location':d.address}
            send_email_to_client(drData,patientData,slotData)
            send_email_to_admin(drData,patientData,slotData)
            send_email_to_dr(drData,patientData,slotData)
            no="+91"+contact_no
            dr_no = "+91"+str(d.contact_no)
            # SMS_notification_to_Dr(no,patientData ,drData, slotData )
            return JsonResponse({'status': 'success'})
        
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e: 
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
@csrf_exempt
def SearchAmbulance(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', '[]'))
            ambulance = Ambulance.objects.filter(location__icontains=data)
            ls=[]
            for i in ambulance:
                j={
                    'name':i.name,
                    'name_owner':i.name_owner,
                    'about_service':i.about_service,
                    'contact':i.contact,
                    'location':i.location
                }
                ls.append(j)
            return JsonResponse({'status': 'success', 'amblance_list': ls})
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
@csrf_exempt
def SearchBloodStorage(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', '[]'))
            BloodStoragel = BloodStorage.objects.filter(location__icontains=data)
            ls=[]
            for i in BloodStoragel:
                j={
                    'name':i.name,
                    'name_owner':i.name_owner,
                    'about_service':i.about_service,
                    'contact':i.contact,
                    'location':i.location
                }
                ls.append(j)
            return JsonResponse({'status': 'success', 'bloodstorage_list': ls})
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
def SearchMedicalStores(request):
    try:
        data = json.loads(request.GET.get('data', '[]'))
        medicalStore = MedicalStore.objects.filter(location__icontains=data)
        ls=[]
        for i in medicalStore:
            j={
                'name':i.name,
                'name_owner':i.name_owner,
                'about_service':i.about_service,
                'hospital_name':i.hospital_name,
                'contact':i.contact,
                'location':i.location
            }
            ls.append(j)
        return JsonResponse({'status': 'success', 'MedicalStorage_list': ls})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
def lab_test(request):
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="doctor not found"
           return render(request,"lab_test.html",{'data':data,'m':m})
        else:
            return render(request,"lab_test.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"lab_test.html")
    
@csrf_exempt
def search_lab(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', '[]'))
            lab = Lab_test.objects.filter(location__icontains=data)
            ls=[]
            for i in lab:
                j={
                    'name':i.name,
                    'name_owner':i.name_owner,
                    'about_service':i.about_service,
                    'contact':i.contact,
                    'location':i.location,
                    'Degree':i.Degree
                }
                ls.append(j)
            return JsonResponse({'status': 'success', 'lab': ls})
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
def healthEquipment(request):
    return render(request,"healthEquipment.html")

@csrf_exempt
def SearchhealthEquipment(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', '[]'))
            healthEquipment = HealthEquipment.objects.filter(location__icontains=data)
            ls=[]
            for i in healthEquipment:
                j={
                   'name':i.name,
                    'name_owner':i.name_owner,
                    'about_service':i.about_service,
                    'contact':i.contact,
                    'location':i.location
                }
                ls.append(j)
            return JsonResponse({'status': 'success', 'healthEquipment_list': ls})
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    except json.JSONDecodeError as e: 
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    
def developer_team(request):
    return render(request,"developer_team.html")

def govenment_hospitals(request):
    h = gov_hopital.objects.all()
    return render(request,"govenment_hospitals.html",{"h":h})


def signinbuttons(request):
    if request.method == 'POST':
        return signinbuttons(request)
    else:
        return render(request,"signinbuttons.html")