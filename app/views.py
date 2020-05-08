"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpRequest
from .models import slide,booking,room
import requests
import smtplib
from django.contrib import messages

from django.core.mail import send_mail
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    """Renders the home page."""
    
    a=slide.objects.all()
    
    
    
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'a':a,
            
        }
    )

def ourhotel(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ourhotel.html',
        {
            'title':'Our hotel',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def bms(request):


    a=slide.objects.all()
    
    return render(
        request,
        'app/bms.html',
        {'a':a,
         'title':'book my stay'})


def reg(request):
    cid=request.GET['cid']
    cod=request.GET['cid']
    destination=request.GET['destination']
    roomtype=request.GET['rt']
    rooms=int(request.GET['room'])

    a=room.objects.filter(room_type=roomtype).filter(status='Unbook').count()
    if a>=rooms:
        return render(
            request,
            'app/reg.html',
            {
                'title':'booking ',
             'cid':cid,
             'cod':cod,
             'destination':destination,
             'roomtype':roomtype,
             'rooms':rooms
         
             }
            )
    else:

        return render(request,'app/norooms.html')

def bc(request):
    sname = request.POST['sname']
    adharno = request.POST['aadharno']
    mobileno = request.POST['mobileno']
    address = request.POST['address']
    destination = request.POST['destination']
    city = request.POST['city']
    state = request.POST['state']
    cid = request.POST['cid']
    cod = request.POST['cod']
    member = request.POST['member']
    roomtype = request.POST['rt']
    username = request.POST['user']
    rooms=int(request.POST['room'])
    Booking=booking(username=username,destination=destination,roomtype=roomtype,name=sname,adharID=adharno,mobileno=mobileno,address=address,city=city,state=state,cid=cid,cot=cod,members=member)
    Booking.save()
    f=''  
    g=booking.objects.filter(roomtype=roomtype).filter(adharID=adharno)
    h=g[0].id
    
    for i in range(rooms):
        c=room.objects.filter(room_type=roomtype).filter(status='Unbook')
        d=c[0].room_no
        
        e=room.objects.get(room_no=d)
        f= f + " , "+ d
        e.status='book'
        e.save()
        booking.objects.filter(id=h).update(room_no=f)
        messages.success(request, "You have been  booked room successfully")
    return render(request,'app/bc.html',{'title':'booking complete',
                                         'rooms':f}) 

def handleSignup(request):

    if request.method == 'POST':

       
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        
       
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

         
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You have been  successfully singup")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
       
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been  successfully login")
            return redirect('home') 
        else:
            messages.success(request, "sorry no account found with these details")
            return redirect('home')
            
    return HttpResponse('404 - Not Found')


def handleLogout(request): 
    logout(request)
    messages.success(request, "You have been  successfully logout")
    return redirect('home')
def contact(request): 
    
    
    return render(request,'app/contact.html',{'title':'contact'})
def yourorder(request): 
    
    
    username = request.GET['user']

    c=set(booking.objects.filter(username=username))
    if c!=set():
        rooms=list(c)[0].room_no
        type=list(c)[0].roomtype
        cid=list(c)[0].cid
        cod=list(c)[0].cot
        
        
        return render(request,"app/yourorder.html",{
            "rooms":rooms,
            "type":type,
            "cid":cid,
            "cot":cod
            
            
            })
    else:
        

        
        return render(request,'app/nobooking.html')

