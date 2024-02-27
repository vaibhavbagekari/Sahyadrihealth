# Generated by Django 4.1.7 on 2024-02-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_newuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='biography',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='languages',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
