# Generated by Django 4.1.7 on 2024-03-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_availability_day_of_week_availability_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='session',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]