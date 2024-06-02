from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# from twilio.rest import Client

def send_email_to_client(drData,patientData,slotData):
    html_content = render_to_string("email_template1.html",{"drData":drData,"patientData":patientData,"slotData":slotData})
    subject = "Confirmation of Your Successfully Booked Doctor Appointment"
    # message = strip_tags(html_content)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patientData["email"]]
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

# def send_sms(to_number, message_body):
#     # Your Account SID and Auth Token from twilio.com/console
#     account_sid = 'AC30f0cbf46e6c80e79bc5ef662e99f18b'
#     auth_token = 'd114e8465c3220d77d8661016f3442a1'
    
#     # Initialize the Twilio client
#     client = Client(account_sid, auth_token)
    
#     # The Twilio phone number you purchased
#     from_number = '+17075498588'
    
#     # Send the SMS
#     message = client.messages.create(
#         body=message_body,
#         from_=from_number,
#         to=to_number
#     )
    
#     # Print the message SID to confirm that the message was sent
#     print(f'Message sent to {to_number}: {message.sid}')
