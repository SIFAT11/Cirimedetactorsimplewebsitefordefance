from django.db import models
import uuid


class GDForm(models.Model):
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    email = models.EmailField()
    district = models.CharField(max_length=255)
    sub_district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    national_id = models.IntegerField()
    birth_date = models.DateField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say')
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    gd_date = models.DateField()
    subject = models.CharField(max_length=255)
    incident_details = models.TextField()
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Taken', 'Taken'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')

    gd_id = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.gd_id:
            # Generate a unique ID using UUID
            unique_id = str(uuid.uuid4())[:4]
            self.gd_id = f'BDGD-{unique_id}'  # Add a hyphen here
        super().save(*args, **kwargs)



    
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)  # Adjust the max_length as needed
    image = models.ImageField(upload_to='profile_images/', default='images/imag-1.jpg')

    def __str__(self):
        return self.full_name
