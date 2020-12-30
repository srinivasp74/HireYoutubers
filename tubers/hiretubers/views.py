from django.shortcuts import render
from .models import Hiretuber
from django.contrib import messages 
from django.shortcuts import redirect
# Create your views here.
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # tuber_id = models.IntegerField()
    # tuber_name = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # phone = models.IntegerField()
    # user_id = models.IntegerField()
    # create_date = models.DateTimeField(blank=True,default = datetime.now)
    # message = models.TextField(blank = True)
 
def hiretuber(request):
    if request.method == 'POST':
       first_name =request.POST['first_name']
       last_name =request.POST['last_name']
       tuber_id =request.POST['tuber_id']
       tuber_name =request.POST['tuber_name']
       city =request.POST['city']
       phone =request.POST['phone']
       email = request.POST['email']
       state =request.POST['state']
       message =request.POST['message']
       user_id =request.POST['user_id']

       # To do : all sanitization

       hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone,email=email,state=state,message=message,user_id=user_id)
       hiretuber.save()
       messages.success(request,'Thanks for reaching out')
       return redirect('youtubers')
    