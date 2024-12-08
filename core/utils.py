from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from google.cloud import translate_v2 as translate
import os

def send_email_to_client(drData,patientData,slotData):
    html_content = render_to_string("email_template1.html",{"drData":drData,"patientData":patientData,"slotData":slotData})
    subject = "Confirmation of Your Successfully Booked Doctor Appointment"
    # message = strip_tags(html_content)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patientData["email"],"healthempire447@gmail.com"]
    send_mail(subject,html_content,from_email,recipient_list, html_message=html_content)

def send_email_to_dr(drData,patientData,slotData):
    html_content = render_to_string("email_template_for_dr.html",{"drData":drData,"patientData":patientData,"slotData":slotData})
    subject = "Confirmation of Your Successfully Booked Appointment"
    # message = strip_tags(html_content)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [drData["email"]]
    send_mail(subject,html_content,from_email,recipient_list, html_message=html_content)

def drAccountOpeningEmail(drData):
    html_content = render_to_string("drAccountOpeningEmail.html",{"drData":drData})
    subject="Welcome to Health Empire - Account Successfully Created!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [drData["email"]]
    print("hii")
    send_mail(subject,html_content,from_email,recipient_list, html_message=html_content)

def SMS_notification(to,patientData,drData,slotData):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    body = "Dear "+ patientData["name"] +" , your appointment with Dr. "+ drData["name"]+" on "+ slotData["date"] +" at "+ slotData["stime"] +" has been successfully booked. If you need to make any changes, please contact us at 9156 42 9156. Thank you, Health Empire Services."
    try:
        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )
        return message.sid
    except TwilioRestException as e:
        return str(e)
    
def SMS_notification_to_Dr(to,patientData,drData,slotData):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    body = "Dr. "+drData["name"]+  " , "+patientData["name"] +" has booked an appointment with you on +"+ slotData["date"] +" at "+ slotData["stime"] +". For any additional information, please contact us at 9156 42 9156. Thank you, Health Empire Services."
    try:
        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )
        return message.sid
    except TwilioRestException as e:
        return str(e)
    

# def translate_text(text, target_language):
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result['translatedText']