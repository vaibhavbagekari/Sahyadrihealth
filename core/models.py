import profile
from xml.dom.minidom import Document
from django.db import models
from django.contrib.auth.models import User
from numpy import true_divide
import os
# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank =True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_no = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    password = models.TextField(null=True,blank=True)

class NewUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank =True,to_field='username',related_name='patients')
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="patient",default="doctor\defaultPicture.png")
    age = models.IntegerField()
    contact_no = models.IntegerField(null=True,blank=True)

class gov_scheme(models.Model):
    name = models.CharField(max_length=100)
    



class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank =True,to_field='username',related_name='doctors')
    address = models.TextField(null=True,blank=True)
    contact_no = models.IntegerField(null=True,blank=True)
    personal_contact = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True,default=00)
    education = models.TextField(max_length=150,null=True,blank=True)
    specialization=models.TextField(max_length=100,null=True,blank=True)
    profile_picture = models.ImageField(upload_to="doctor",default="doctor\defaultPicture.png",blank=True)
    license_no= models.IntegerField(null=True,blank=True,default=0)
    mapLink=models.TextField(null=True,blank=True,max_length=500)
    opdFees=models.IntegerField(null=True,blank=True)
    category=models.TextField(max_length=100,null=True,blank=True)
    experience=models.TextField(max_length=100,null=True,blank=True)
    languages=models.TextField(max_length=100,null=True,blank=True)
    biography=models.TextField(max_length=1000,null=True,blank=True)
    hospital_name=models.TextField(max_length=150,null=True,blank=True)
    hospital_about = models.TextField(max_length=1000,null=True,blank=True)
    slotDuration = models.IntegerField(null=True,blank=True,default=10)
    def delete(self, *args, **kwargs):
        # Check if the profile picture is not the default one
        if self.profile_picture and not self.profile_picture.name == 'doctor/defaultPicture.png':
            # Get the path to the profile picture file
            path = self.profile_picture.path
            # Check if the file exists
            if os.path.exists(path):
                # Delete the file
                os.remove(path)
        # Call the superclass delete method to delete the Doctor record
        super(Doctor, self).delete(*args, **kwargs)

class dr_scheme_mapping(models.Model):
    gov_scheme = models.ForeignKey(gov_scheme,on_delete=models.CASCADE,related_name="scheme_mapping")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="dr_mapping")

class Event(models.Model):
    user = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank =True,to_field='id',related_name='events')
    title = models.CharField(max_length=255,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    color = models.CharField(max_length=20, default='#2ecc71',null=True,blank=True)  # Default color for open slots
    patient_booked=models.CharField(max_length=50,null=True,blank=True)
    time_of_booking=models.DateTimeField(null=True,blank=True)
    

class Hospital_Image(models.Model):
    user = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank =True,to_field='id',related_name='Himgs')
    title = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='hospital_images/')
    def delete(self,*args,**kwargs):
        if self.image.path:
            path = self.image.path
            if os.path.exists(path):
                os.remove(path)
        super(Hospital_Image,self).delete(*args, **kwargs)

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor,to_field="id", on_delete=models.CASCADE,related_name='doctor')
    session = models.CharField(max_length=10,null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Availability_weekly(models.Model):
    doctor = models.ForeignKey(Doctor,to_field="id", on_delete=models.CASCADE,related_name='doctorW')
    json = models.JSONField( null=True,blank=True)


class Contact(models.Model):
    fullname = models.CharField(max_length=150,null=True,blank = True)
    contact = models.IntegerField(null = True,blank = True)
    message = models.CharField(max_length=150,null=True,blank = True)

class Ambulance(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    name_owner=models.CharField(max_length=150,null=True,blank=True)
    about_service=models.CharField(null=True, max_length=900,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)

class AmbulanceImage(models.Model):
    image = models.ForeignKey(Ambulance,to_field='id',related_name='image',on_delete=models.CASCADE)
    mainimage = models.ImageField(upload_to='ambulance/', null = True,blank=True)
    def delete(self,*args,**kwargs):
        if self.mainimage.path:
            path = self.mainimage.path
            if os.path.exists(path):
                os.remove(path)
        super(AmbulanceImage,self).delete(*args, **kwargs)

class BloodStorage(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    name_owner=models.CharField(max_length=150,null=True,blank=True)
    about_service=models.CharField(null=True, max_length=900,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)

class BloodStorageImage(models.Model):
    image = models.ForeignKey(BloodStorage,to_field='id',related_name='image',on_delete=models.CASCADE)
    mainimage = models.ImageField(upload_to='bloodStorage/', null = True,blank=True)

    def delete(self , using=None):
        # Delete associated files
        if self.mainimage:
            os.remove(self.mainimage.path)
        # Call parent delete method to delete the object from the database
        super().delete(using=using)


class CustomManager(models.Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()

class BookedAppoinment(models.Model):
    doctor = models.ForeignKey(Doctor,to_field="id", on_delete=models.CASCADE,related_name='dr')
    date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    Patient_name = models.CharField(max_length=150,null=True,blank=True)
    Patient_contact = models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)

class Government_schemes(models.Model):
    title=models.TextField(null=True,blank=True)
    title_img=models.FileField(upload_to="Government_schemes\images",default="govschem\images\defaultimg.jpg")
    sub_title = models.TextField(max_length=1000,null=True,blank=True)
    Document = models.FileField(null=True,blank=True)
    objects= CustomManager()

    def delete(self , using=None):
        # Delete associated files
        if self.title_img:
            os.remove(self.title_img.path)
        if self.Document:
            os.remove(self.Document.path)
        # Call parent delete method to delete the object from the database
        super().delete(using=using)



class Dr_govScheme(models.Model):
    doctor = models.ForeignKey(Doctor,to_field="id", on_delete=models.CASCADE,related_name='drGov')
    title=models.TextField(null=True,blank=True)
    title_img=models.FileField(upload_to="govschem\images",default="govschem\images\defaultimg.jpeg")
    sub_title = models.TextField(max_length=1000,null=True,blank=True)
    Document = models.FileField(upload_to="govschem\documents",default="govschem\documents\blank.pdf")

    objects= CustomManager()

    def delete(self , using=None):
        # Delete associated files
        if self.title_img:
            os.remove(self.title_img.path)
        if self.Document:
            os.remove(self.Document.path)
        # Call parent delete method to delete the object from the database
        super().delete(using=using)

class Dr_Insurance(models.Model):
    doctor = models.ForeignKey(Doctor,to_field="id", on_delete=models.CASCADE,related_name='drInsurance')
    title=models.TextField(null=True,blank=True)
    title_img=models.FileField(upload_to="insurance\images",default="insurance\images\defaultimg.jpg")
    sub_title = models.TextField(max_length=1000,null=True,blank=True)
    Document = models.FileField(upload_to="insurance\documents",default="insurance\documents\blank.pdf")

    objects= CustomManager()

    def delete(self , using=None):
        # Delete associated files
        if self.title_img:
            os.remove(self.title_img.path)
        if self.Document:
            os.remove(self.Document.path)
        # Call parent delete method to delete the object from the database
        super().delete(using=using)

class Lab_test(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    name_owner=models.CharField(max_length=150,null=True,blank=True)
    about_service=models.CharField(null=True, max_length=900,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)
    Degree = models.CharField(max_length=100,null=True,blank=True)

class HealthEquipment(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    name_owner=models.CharField(max_length=150,null=True,blank=True)
    about_service=models.CharField(null=True, max_length=900,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)
    
class feedbackquestion(models.Model):
    question = models.TextField(null=True,blank=True)

class feedbackans(models.Model):
    question = models.ForeignKey(feedbackquestion,to_field="id", on_delete=models.CASCADE,related_name='fbans')
    doctorid = models.IntegerField(null=True,blank=True)
    ans = models.CharField(max_length=4,null=True,blank=True)


    