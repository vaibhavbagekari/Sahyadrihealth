from audioop import reverse
from django.shortcuts import render, redirect
from .models import *
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

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

def drProfile(request,id):
    doctor=User.objects.filter(id=id)
    slider_img=User.objects.get(id=id).doctors.all()[0].Himgs.all()
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
