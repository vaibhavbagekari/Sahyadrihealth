# Generated by Django 4.1.7 on 2024-10-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_gov_hopital'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('name_owner', models.CharField(blank=True, max_length=150, null=True)),
                ('hospital_name', models.CharField(blank=True, max_length=200, null=True)),
                ('about_service', models.CharField(blank=True, max_length=900, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]