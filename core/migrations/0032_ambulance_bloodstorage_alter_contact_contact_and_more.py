# Generated by Django 4.1.7 on 2024-03-23 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('name_owner', models.CharField(blank=True, max_length=150, null=True)),
                ('about_service', models.CharField(blank=True, max_length=900, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='bloodStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('name_owner', models.CharField(blank=True, max_length=150, null=True)),
                ('about_service', models.CharField(blank=True, max_length=900, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='bloodStorageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, null=True, upload_to='bloodStorage/')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.bloodstorage')),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, null=True, upload_to='ambulance/')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.ambulance')),
            ],
        ),
    ]
