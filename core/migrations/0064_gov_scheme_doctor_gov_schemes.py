# Generated by Django 4.1.7 on 2024-08-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_alter_doctor_license_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='gov_scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='gov_schemes',
            field=models.ManyToManyField(related_name='doctors_schemes', to='core.gov_scheme'),
        ),
    ]
