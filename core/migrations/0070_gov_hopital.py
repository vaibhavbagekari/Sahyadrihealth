# Generated by Django 4.1.7 on 2024-08-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_health_insurance_dr_insurance_mapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='gov_hopital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(blank=True, max_length=500, null=True)),
                ('Doctor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
