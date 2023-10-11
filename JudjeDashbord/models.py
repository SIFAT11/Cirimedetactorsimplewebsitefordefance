from django.db import models
from django.contrib.auth.models import User

class JudgeProfile(models.Model):
    jugid = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', default='images/imag-1.jpg')
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Taken', 'Taken'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.jugid.username 
