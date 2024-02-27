import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank =True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_no = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    password = models.TextField(null=True,blank=True)

class NewUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank =True,to_field='username',related_name='patients')
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="patient",default="doctor\defaultPicture.png")
    age = models.IntegerField()
    contact_no = models.IntegerField(null=True,blank=True)

class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank =True,to_field='username',related_name='doctors')
    address = models.TextField(null=True,blank=True)
    contact_no = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    education = models.TextField(max_length=150,null=True,blank=True)
    specialization=models.TextField(max_length=100,null=True,blank=True)
    profile_picture = models.ImageField(upload_to="doctor")
    license_no= models.IntegerField(null=True,blank=True)
    category=models.TextField(max_length=100,null=True,blank=True)
    experience=models.TextField(max_length=100,null=True,blank=True)
    languages=models.TextField(max_length=100,null=True,blank=True)
    biography=models.TextField(max_length=1000,null=True,blank=True)


class Event(models.Model):
    user = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,blank =True,to_field='id',related_name='events')
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    color = models.CharField(max_length=20, default='#2ecc71')  # Default color for open slots
