from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Mail,Documents
from .forms import LoginForm
from django.contrib import auth
# Create your views hdef 

def homeview(request):
    if request.method=="POST":
        name = request.POST['name1']
        mail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        email = EmailMessage(subject, message, to=['shashankpathe9424@gmail.com'])
        
        email.send()
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('/')       
    return render(request,"index.html")         
   

def DocumentsView(request):

    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  
            password = form.cleaned_data['password'] 
            print(username)
            user= auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                if user.is_superuser:
                    messages.add_message(request, messages.INFO, 'logged in success')
                    return redirect("admin/")
                else:
                    messages.add_message(request, messages.INFO, 'logged in success')  
                    return redirect('/d')
            else:
                form= LoginForm()
                context = {'form':form}
                messages.add_message(request, messages.WARNING, 'invalid credentials')     
                return render(request,"loginview.html",context)

        else:
            form= LoginForm()
            context = {'form':form}     
            return render(request,"loginview.html",context)
    else:
        form=LoginForm()
        context = {'form':form} 
        return render(request,"loginview.html",context)
    form=LoginForm()
    context = {'form':form} 
    return render(request,"loginview.html",context)
            
def Docs(request):
    data= Documents.objects.all()
    print(data)
    context={'document':data}
    return render(request,'documents.html',context)
