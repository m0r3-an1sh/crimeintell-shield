from django.contrib import admin
from django.urls import include, path
from home import views
from MLBackend import Graph_crime1,face_recognition,CrimeSearch,CrimePredict


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('contact', views.contact, name='contact'),
    path('crime_search',CrimeSearch.crime_search ,name='crime_search'),
    path('graph',Graph_crime1.Graph ,name='graph'),
    path('videofeed', face_recognition.video_feed ,name='videofeed'),
    path('crime_detect', face_recognition.crimedetect ,name='crime_detect'),
    path('crime_predict', CrimePredict.crime_predict ,name='crime_predict'),
    path('signup', views.signup ,name='signup'),
    path('login', views.userlogin ,name='login'),
    path('logout', views.userlogout ,name='logout'),
    path('contactform', views.contactform ,name='contactform'),
    path('services', views.services ,name='services'),
    path('servicedetails', views.servicedetails ,name='servicedetails'),
    path('projects', views.projects ,name='project'),
    path('comment', views.postcomment ,name='comment'),
    path('crimereport',views.crimereport,name='crimereport'),
    path('unsafereport',views.unsafereport,name='unsafereport')
]
