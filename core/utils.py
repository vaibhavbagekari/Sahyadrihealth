from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import pywhatkit

def send_email_to_client(k,d,p):
    html_content = render_to_string("email_template.html",{"event":k,"doctor":d,"patient":p})
    subject = "Confirmation of Your Successfully Booked Doctor Appointment"
    message = strip_tags(html_content)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["surajnimbalkar805@gmail.com","testwebbyvaibhav@gmail.com","aniketthorat2122@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)

def whatsApp_mag():
    pywhatkit.sendwhatmsg("this is automate whatsapp message from Sahyadri Health services")