from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        #check if user has already made enquiry
        if request.user.is_authenticated:
            
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'your request has already been submitted for this listing')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        #send mail
        send_mail('property listing enquiry','there has been an enquiry for' + listing + 'sign to the admin panel for more info',
            'gprateek558@gmail.com',[realtor_email,'guptaprateek9828@gmail.com'],fail_silently=False)

        messages.success(request,'your request has been submitted')
        return redirect('/listings/'+listing_id)


    else:
        return redirect('register')