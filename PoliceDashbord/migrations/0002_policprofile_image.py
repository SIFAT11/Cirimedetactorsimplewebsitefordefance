# Generated by Django 4.2.6 on 2023-10-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoliceDashbord', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='policprofile',
            name='image',
            field=models.ImageField(default='images/imag-1.jpg', upload_to='profile_images/'),
        ),
    ]
