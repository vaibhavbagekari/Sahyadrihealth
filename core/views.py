from operator import ne
from os import name
from pydoc import render_doc
from urllib import request
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.shortcuts import redirect, render
from matplotlib import category
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.

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
    print(id)
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

def home(request):
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="docter not found"
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
           m="docter not found"
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
           m="docter not found"
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
           m="docter not found"
           return render(request,"findDrNearYou.html",{'data':data,'m':m})
        else:
            return render(request,"findDrNearYou.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
        
     elif request.GET.get('Flocation'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('Flocation'),category__icontains=request.GET.get('Fcategory'))
        count=len(data)
        ad=request.GET.get('Flocation')
        if not data.exists():
           m="docter not found"
           return render(request,"findDrNearYou.html",{'Fdata':data,'Fm':m})
        else:
            l=get_locations()
            return render(request,"findDrNearYou.html",{'Fdata':data,'Fcount':count,'Fad':ad,'Flocations':l})
         
     else:
        return render(request,"findDrNearYou.html")

def contactUs(request):
     if request.method == 'POST':
        return check_form(request)
     elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="docter not found"
           return render(request,"contactUs.html",{'data':data,'m':m})
        else:
            return render(request,"contactUs.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
     else:
        return render(request,"contactUs.html")

def goverment_scheme(request):
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="docter not found"
           return render(request,"goverment_scheme.html",{'data':data,'m':m})
        else:
            return render(request,"goverment_scheme.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"goverment_scheme.html")
    

def search_ambulance(request):
    if request.method == 'POST':
        return check_form(request)
    elif request.GET.get('location'):
        data=Doctor.objects.filter(address__icontains=request.GET.get('location'),category__icontains=request.GET.get('category'))
        count=len(data)
        ad=request.GET.get('location')
        if not data.exists():
           m="docter not found"
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
           m="docter not found"
           return render(request,"blood_storage.html",{'data':data,'m':m})
        else:
            return render(request,"blood_storage.html",{'data':data,'count':count,'ad':ad,'locations':get_locations()})
    else:
        return render(request,"blood_storage.html")

def demo(request):
    check_form(request)
    queryset=Patient.objects.all()
    patient={'patient':queryset}
    return render(request,"demo.html",patient)

@ensure_csrf_cookie
@csrf_protect 
def drSigUp(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('FName')
        last_name = data.get('LName')
        age = data.get('age')
        email=data.get('email')
        profile_picture = request.FILES.get('Pfile')
        education = data.get('education')
        address = data.get('address')
        contact_no = data.get('contact_no')
        license_no = data.get('licenseNumber')
        password=data.get('password')
        username=data.get('email')
        specialization=data.get('specialization')
        catagory = data.get('catagory')
        
        obj = User.objects.filter(username=username)
        print(profile_picture)
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
                age=age,
                profile_picture=profile_picture,
                education=education,
                address=address,
                contact_no=contact_no,
                license_no=license_no,
                specialization=specialization,
                category=catagory
            )
            
           
            doctor.save()

            msg="Account created Successfuly"
            messages.add_message(request, messages.INFO, msg)
            return render(request,"drsignin.html")
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

@csrf_exempt  # For simplicity. You may want to use a proper CSRF token in production.
@require_POST
def save_events(request,id):
    try:

     if request.method == 'POST':
            data = json.loads(request.POST.get('events', '[]'))
            print(data)
            # Clear existing events in the database (if needed)
            dr = Doctor.objects.get(id=id)
            dr.events.all().delete()
            # Save new events to the database
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


def drProfile(request,id):
    doctor=User.objects.filter(id=id)
    return render(request,"drProfile.html",{'doctor':doctor})