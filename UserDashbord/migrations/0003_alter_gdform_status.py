# Generated by Django 4.2.6 on 2023-10-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDashbord', '0002_alter_gdform_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gdform',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Taken', 'Taken'), ('Rejected', 'Rejected')], default='Pending', max_length=8),
        ),
    ]
