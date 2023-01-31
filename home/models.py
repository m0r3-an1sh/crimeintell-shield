from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content1 = models.TextField()
    content2 = models.TextField()
    heading1 = models.CharField(max_length=180)
    content3 = models.TextField()
    heading2 = models.CharField(max_length=180)
    content4 = models.TextField()
    quotes = models.CharField(max_length=150)
    thumbimage=models.ImageField(upload_to ='static/uploads/thumb')
    mainimage=models.ImageField(upload_to = 'static/uploads/main')
    descimage=models.ImageField(upload_to ='static/uploads/desc')
    thumbimagelink=models.CharField(default ='uploads/thumb/', max_length=280)
    mainimagelink=models.CharField(default = 'uploads/main/', max_length=280)
    descimagelink=models.CharField(default ='uploads/desc/', max_length=280)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Blogcomments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        a = self.comment[0:13]+"..."+" by "+self.user.username+" on "+str(self.post)
        return a

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    msg = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    sno = models.AutoField(primary_key=True)
    tes_image=models.ImageField(upload_to ='static/uploads/main')
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    tes_msg = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class userprotection(models.Model):
    sno = models.AutoField(primary_key=True)
    userrname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    livingloc = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class reportingcrime(models.Model):
    sno = models.AutoField(primary_key=True)
    reportername = models.CharField(max_length=100)
    crimeloc = models.CharField(max_length=100)
    crimedetail = models.TextField()
    crimeproof = models.ImageField(upload_to ='static/uploads/reportcrime')

    def __str__(self):
        a=self.reportername + self.crimeloc
        return a

class usersafety(models.Model):
    sno = models.AutoField(primary_key=True)
    usersafetyname= models.CharField(max_length=100)
    usertelegramclientid = models.CharField(max_length=100)
    otherstelegramclientid = models.TextField()
    message = models.TextField()

    def __str__(self):
        a=self.usersafetyname + self.usertelegramclientid
        return a
