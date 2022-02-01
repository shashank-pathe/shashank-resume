from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Mail
# Create your views hdef 

def homeview(request):
    if request.method=="POST":
        name = request.POST['name']
        mail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Mail(name=name,email=mail,subject=subject,message=message)
        
        data.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('/')       
    return render(request,'index.html')