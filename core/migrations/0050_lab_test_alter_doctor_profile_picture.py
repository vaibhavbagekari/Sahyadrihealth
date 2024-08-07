# Generated by Django 4.1.7 on 2024-04-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_alter_dr_govscheme_document_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_test',
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
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, default='doctor\\defaultPicture.png', upload_to='doctor'),
        ),
    ]
