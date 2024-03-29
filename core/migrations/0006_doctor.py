# Generated by Django 4.1.7 on 2024-02-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('education', models.TextField(max_length=150)),
                ('specialization', models.TextField(max_length=100)),
                ('profile_picture', models.FileField(default='https://tse1.explicit.bing.net/th?id=OIP.M_cxPuULfylrc9mKkOuqGgHaGd&pid=Api&P=0&h=180', upload_to='')),
                ('license_no', models.IntegerField(blank=True, null=True)),
                ('category', models.TextField(max_length=100)),
            ],
        ),
    ]
