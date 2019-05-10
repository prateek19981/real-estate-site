from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact
from contact import views

# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']


        if password==password2:
            if User.objects.filter(username=username):
                messages.error(request,'that username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request,'that email already exits')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,'registered succesfully,u can now login')
                    return redirect('login')

                

        else:
            messages.error(request,'passwords do not match')
            return redirect('register')

    return render(request,'account/register.html')



def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            
            
            auth.login(request,user)
            messages.success(request,'logged in succesfully')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    return render(request,'account/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'logged out successfully')

        return redirect('index')










def dashboard(request):
    user_contacts=Contact.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
    return render(request,'account/dashboard.html',{'contact':user_contacts})
