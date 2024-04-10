# Generated by Django 4.1.7 on 2024-02-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_doctor_biography_doctor_experience_doctor_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('color', models.CharField(default='#2ecc71', max_length=20)),
            ],
        ),
    ]