from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Mail
from .forms import LoginForm
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



def loginview(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  
            password = form.cleaned_data['password'] 
            print(username)
            user= auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                return render(request,'loginview.html')
            else:
                form= LoginForm()
                context = {'form':form}
                messages.add_message(request, messages.WARNING, 'invalid credentials')     
                return render(request,"loginview.html",context)

        else:
            form= LoginForm()
            context = {'form':form}     
            return render(request,"base.html",context)
    else:
        form= LoginForm()
        context = {'form':form}
        messages.add_message(request, messages.WARNING, 'invalid credentials')     
        return render(request,"loginview.html",context)
            