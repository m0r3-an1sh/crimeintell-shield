from django.shortcuts import render,HttpResponse,redirect
from home.models import Blog,Contact,Testimonial,Blogcomments,userprotection,reportingcrime,usersafety
from django.contrib import messages,admin
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from geopy.geocoders import Nominatim
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import asyncio


#adminpagecustom

admin.site.site_header = "C!S Admin"
admin.site.site_title = "C!S Admin Panel"
admin.site.index_title = "Welcome to Crime Intell!Shield"


revblog = Blog.objects.filter().order_by('-sno')[:4:1]


# Create your views here.
def home(request):
    alltestimonial = Testimonial.objects.all()
    recblog = Blog.objects.filter().order_by('-sno')[:3:1]
    dict = {'testimonials':alltestimonial,'recblog':recblog,'revblog':revblog}
    return render(request,'home.html',dict)

def about(request):
    alltestimonial = Testimonial.objects.all()
    dict = {'testimonials':alltestimonial,'revblog':revblog}
    return render(request,"about.html",dict)

def blog(request):
    allblogs = Blog.objects.order_by('sno')
    p = Paginator(allblogs,3)
    pno = request.GET.get('page')
    page = p.page(pno)
    print(page,pno)
    a=[]
    for i in range (1,p.num_pages+1):
        a.append(i)       
    print(a)

    dictionary = {'blogs':allblogs,'page':page,'nopages':a,'revblog':revblog} 
    return render(request,'blog.html',dictionary)

def blogpost(request,slug):
    Murdercount = Blog.objects.filter(category="Murder").count()
    Kidnappingcount = Blog.objects.filter(category="Kidnapping").count()
    Dacoitycount = Blog.objects.filter(category="Dacoity").count()
    Analyticscount = Blog.objects.filter(category="Analytics").count()
    Rapecount = Blog.objects.filter(category="Rape").count()
    Molestationcount = Blog.objects.filter(category="Molestation").count()
    

    blog = Blog.objects.filter(slug=slug).first()
    comment = Blogcomments.objects.filter(post=blog)
    recblog = Blog.objects.filter().order_by('-sno')[:4:1]
    metatag= blog.tags.split()  
    dict = {'blog':blog,'comment':comment,'recblog':recblog,'metatag':metatag,'commentcount':comment.count()
    ,'Murdercount':Murdercount,'Kidnappingcount':Kidnappingcount,'Dacoitycount':Dacoitycount,'Analyticscount':Analyticscount,'Rapecount':Rapecount,'Molestationcount':Molestationcount,'revblog':revblog}
    return render(request,"blogpost.html",dict)

def postcomment(request):
    if request.method=="POST":

        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("sno")
        post = Blog.objects.get(sno=postsno)
        print(comment)

        comment = Blogcomments(comment=comment,user=user,post=post)
        comment.save()

    return redirect(f"/blogpost/{post.slug}")

def contact(request):
    dicti = {'revblog':revblog}
    return render(request,'contact.html',dicti)

def signup(request):
    if request.method=="POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        loc = request.POST['loc']
        userteleid = request.POST['userteleid']
        otherteleid = request.POST['otherteleid']
        EmerMes = request.POST['EmerMes']
        
        #usersignup
        myuser = User.objects.create_user(uname,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        protecuser = userprotection(userrname=uname,name=fname,email=email,livingloc=loc)
        protecuser.save()

        userrsafety = usersafety(usersafetyname=fname,usertelegramclientid=userteleid,otherstelegramclientid=otherteleid,message=EmerMes)
        userrsafety.save()

        messages.success(request,f"{uname} added successfully")
        return redirect('home')
    else:
        return HttpResponse("fail")

def userlogin(request):
    if request.method=="POST":
        logemail = request.POST['email1']
        logpass = request.POST['logpass1']
        user = authenticate(request,username=logemail,password=logpass)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in")
            return redirect('home')
        else:
            messages.success(request,"Invalid credentials")
            return redirect('home')
    return HttpResponse('404-notfound')

def userlogout(request):
    if request.method =="POST":
        logout(request)
        messages.success(request,"logged out")
    return redirect('home')

def contactform(request):
    if request.method=="POST":
        conname = request.POST['conname']
        conemail = request.POST['conemail']
        conphone = request.POST['conphone']
        conmsg = request.POST['conmessage']
        con = Contact(name=conname,email=conemail,contact=conphone,msg=conmsg)
        con.save()
    return redirect('home')

def services(request):
    alltestimonial = Testimonial.objects.all()
    dict = {'testimonials':alltestimonial,'revblog':revblog}
    return render(request,"services.html",dict)

def servicedetails(request):
    dict = {'revblog':revblog}
    return render(request,"service-details.html",dict)

def projects(request):
    return render(request,"projects.html")

def crimereport(request):
    dict = {'revblog':revblog}
    if request.method=="POST":
        reportuname = request.user
        crimeloc = request.POST['crimeloc']
        crimedet = request.POST['crimedet']
        crimeproof = request.FILES['crimeproof']

        reportcrime = reportingcrime(reportername=reportuname,crimeloc=crimeloc,crimedetail=crimedet,crimeproof=crimeproof)
        reportcrime.save()

        mail = userprotection.objects.all().filter(livingloc=crimeloc)
        receivermail = []
        for i in range(mail.count()):
            receivermail.append(mail[i].email)
        
        if len(receivermail)!=0:
                subject, from_email = f'{crimedet} happening in your area', 'randomkidd1209@gmail.com'
                html_content = f'<h2>This is a crime alert mail.</h2><h3>{crimedet} has happended in your vicinity so do be careful.</h3><p>We are going to inform the authorities shortly so do be careful.</p>'
                msg = EmailMessage(subject, html_content, from_email, receivermail)
                msg.content_subtype = "html"
                msg.send()

        

    return render (request,"crimereport.html",dict)

def unsafereport(request):
    dict={'revblog':revblog}
    if request.method=="POST":
        user = request.user
        usersafe = usersafety.objects.all().filter(usersafetyname=user.first_name)
        usname = usersafe[0].usersafetyname
        ustelcliid = usersafe[0].usertelegramclientid 
        usothcliid = usersafe[0].otherstelegramclientid.split()
        usmes = usersafe[0].message
        lat=request.POST["lat"]
        long=request.POST["long"]
        # print(lat,long)
        try:
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(lat+","+long)
            print(location)
        except:
            location = "check it out using the link"
        #emergency msg and telegram client id

        api_id = '28199235'
        api_hash = 'da53a85eb88e745df9a25629edae73af'
        token = '5846045827:AAGcX_3fN4DwETPfxGTtgVOFloitZtB10cA'
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        message = "This is am emergency from "+str(usname)+"\n"+"message: "+str(usmes)+"\n"+"location: "+str(location)+"\nlat: "+str(lat)+"\nlong: "+str(long)+f"\nnavigate: https://www.google.com/maps/@{lat},{long},15z"
        phone = '+919152209434'
        client = TelegramClient('session',api_id, api_hash, loop=loop)
        client.connect()
        for i in range(len(usothcliid)):
            receiver = InputPeerUser(int(usothcliid[i]), 0)
            client.send_message(receiver, message, parse_mode='html')
        
        client.disconnect()

    return render (request,"unsafereport.html",dict)