from googleapiclient.discovery import build
from django.shortcuts import render,HttpResponse
from home.models import Blog
revblog = Blog.objects.filter().order_by('-sno')[:4:1]

my_api_key = "AIzaSyBr7F9uU4ugzENnue1dx2QBxfu5Ay0M7Xs"
my_cse_id = "d65b510145a7d499c"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

def crime_search(request):
    c={None:None}
    dict={None:None,'revblog':revblog}
    def search_results(result):
        result = result
        title=[]
        link=[]
        img=[]
        desc = []
        for i in range(10):
            try:
                title.append(result["items"][i]["title"])
            except:
                title.append("Crime everywhere")

            try:    
                link.append(result["items"][i]["link"])
            except:
                link.append("https://zeenews.india.com/latest-news")

            try:
                img.append(result["items"][i]["pagemap"]["cse_thumbnail"][0]["src"])
            except:
                img.append("https://media.istockphoto.com/id/1059636358/photo/crime-scene-tape-barrier-in-front-of-defocused-background.jpg?s=612x612&w=0&k=20&c=OY-zRCjZomRECgreeVysbpBelxrGhdeIn6sQBMC5lUE=")

            try:    
                desc.append(result["items"][i]["pagemap"]["metatags"][0]["og:description"]+"\n")
            except:
                desc.append("Crime rates are increasing day by day. Everyday the common man is suffering from criminals.the gov...")
        dict = {"title":title,"link":link,"img":img,"desc":desc,'revblog':revblog} 
        return dict

    # result = google_search("info:news intext:crime|frauds|cybercrime|murder|theft|dacoity intext:mumbai daterange:22335-23015", my_api_key, my_cse_id)
    

    if request.method=="POST":
        try:
            a = request.POST["location"] 
            print(a)

            b = request.POST["crime"] 
            print(b)

            result = google_search(f"info:news intext:{b} intext:{a} daterange:23001-23024", my_api_key, my_cse_id)
            # julian date format

            c=search_results(result)
            dict={"c":c,'revblog':revblog}
            print(dict["c"]['title'])
            # for i in range(10):
            #     print(c["title"][i])
            #     print(c["link"][i])
            #     print(c["img"][i])
            #     print(c["desc"][i])
        except:
            dict = {'error':'Select the options appropriately'}
            return render(request,"notfound.html",dict)

    return render(request,'search.html',dict)

	
