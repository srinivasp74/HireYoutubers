from django.db import models

# Create your models here.
class Contactus(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    detailed_message = models.TextField(blank = True)
    

    def __str__(self):
        return self.email