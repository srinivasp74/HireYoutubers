from django.shortcuts import render
from .models import Contactus
from django.shortcuts import redirect
from django.contrib import messages 
    # full_name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # Company = models.CharField(max_length=100)
    # Subject = models.CharField(max_length=100)
    # Detailed_message = models.TextField(blank = True)
# Create your views here.
def contactus(request):
     if request.method == 'POST':
        full_name = request.POST['full_name'] 
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        detailed_message = request.POST['detailed_message']

#to do: sanitization
        contactus = Contactus(full_name=full_name,phone = phone,email= email,company=company,subject=subject,detailed_message=detailed_message)
        contactus.save()
        messages.success(request,'Thanks for reaching us out!')
        return redirect('youtubers')