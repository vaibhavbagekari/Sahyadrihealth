# Generated by Django 4.1.7 on 2024-02-08 07:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_alter_doctor_profile_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='doctor',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='category',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='education',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
