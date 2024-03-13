# views.py
from django.shortcuts import render
from .models import Doctor, Appointment
from datetime import datetime, timedelta

def doctor_availability(request, doctor_id):
    # Get the doctor object
    doctor = Doctor.objects.get(pk=doctor_id)

    # Get today's date for initial availability display
    today = datetime.now().date()

    # Get available time slots for the next 7 days
    available_slots = get_available_slots(doctor, today, days=7)

    context = {
        'doctor': doctor,
        'available_slots': available_slots,
        'selected_date': today,
    }

    return render(request, 'doctor_availability.html', context)

def get_available_slots(doctor, date, days=7):
    # Define the time slot interval (e.g., 30 minutes)
    time_slot_interval = timedelta(minutes=30)

    available_slots = []

    for day in range(days):
        current_date = date + timedelta(days=day)

        # Get all appointments for the doctor on the current date
        appointments_on_date = Appointment.objects.filter(doctor=doctor, date=current_date)

        # Generate time slots for the current date
        start_time = doctor.office_hours_start
        end_time = doctor.office_hours_end

        current_time = start_time
        while current_time < end_time:
            end_of_slot = current_time + time_slot_interval
            slot = {'start_time': current_time, 'end_time': end_of_slot, 'date': current_date}
            
            # Check if the slot is available (not overlapping with any appointments)
            if all(appointment.end_time <= current_time or appointment.start_time >= end_of_slot for appointment in appointments_on_date):
                available_slots.append(slot)

            current_time = end_of_slot

    return available_slots
