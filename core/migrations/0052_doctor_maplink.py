# Generated by Django 4.1.7 on 2024-04-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_lab_test_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='mapLink',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]