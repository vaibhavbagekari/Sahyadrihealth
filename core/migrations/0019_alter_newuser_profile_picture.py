# Generated by Django 4.1.7 on 2024-02-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_newuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='profile_picture',
            field=models.ImageField(default='sahyadrihealth\\core\\static\\default-profile-picture.png', upload_to='patient'),
        ),
    ]
