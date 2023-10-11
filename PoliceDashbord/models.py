from django.db import models

class PolicProfile(models.Model):
    policeid = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_images/', default='images/imag-1.jpg')
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Taken', 'Taken'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')
    def __str__(self):
        return self.policeid
