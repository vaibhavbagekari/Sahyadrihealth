from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email_to_client(drData,patientData,slotData):
    html_content = render_to_string("email_template1.html",{"drData":drData,"patientData":patientData,"slotData":slotData})
    subject = "Confirmation of Your Successfully Booked Doctor Appointment"
    # message = strip_tags(html_content)
    from_email = settings.EMAIL_HOST_USER
    print(type(patientData["email"]))
    recipient_list = [drData["email"],patientData["email"]]
    send_mail(subject,html_content,from_email,recipient_list, html_message=html_content)
