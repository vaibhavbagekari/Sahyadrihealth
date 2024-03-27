# Generated by Django 4.1.7 on 2024-03-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_availability_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='core.doctor'),
        ),
        migrations.CreateModel(
            name='Availability_weekly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorW', to='core.doctor')),
            ],
        ),
    ]
