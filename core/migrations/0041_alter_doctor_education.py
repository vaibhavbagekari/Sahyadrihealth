# Generated by Django 4.1.7 on 2024-04-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_remove_doctor_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='education',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
