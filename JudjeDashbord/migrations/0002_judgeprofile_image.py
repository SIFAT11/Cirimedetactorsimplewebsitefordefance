# Generated by Django 4.2.6 on 2023-10-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JudjeDashbord', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgeprofile',
            name='image',
            field=models.ImageField(default='images/imag-1.jpg', upload_to='profile_images/'),
        ),
    ]
