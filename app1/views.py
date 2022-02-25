from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Mail,Documents
from .forms import LoginForm
from django.core.mail import EmailMessage
from django.contrib import auth
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import  strip_tags
from resume import settings
# Create your views hdef 

def homeview(request):
    if request.method=="POST":
        name = request.POST['name1']
        mail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        html_comtent = render_to_string("log.html",{
            "name":name,"mail":mail,"subject":subject,"message":message
        })
        text_content = strip_tags(html_comtent)
        email = EmailMultiAlternatives("Hiring from my website",text_content,settings.EMAIL_HOST_USER, to=['shashankpathe9424@gmail.com'])
        email.attach_alternative(html_comtent,"text/html")
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
