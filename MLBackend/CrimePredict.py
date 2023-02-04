from django.shortcuts import render,HttpResponse
import pickle
from home.models import Blog
revblog = Blog.objects.filter().order_by('-sno')[:4:1]

def crime_predict(request):
    with open('D:\\CODE\\Django\\django code\\bloggingwebsite\\MLBackend\\totalcrimepred.pickle','rb') as f:
        total = pickle.load(f)
    with open('D:\\CODE\\Django\\django code\\bloggingwebsite\\MLBackend\\murderpredictmodel.pickle','rb') as f:
        murder = pickle.load(f)
    with open('D:\\CODE\\Django\\django code\\bloggingwebsite\\MLBackend\\rapepredictmodel.pickle','rb') as f:
        rape = pickle.load(f)
    with open('D:\\CODE\\Django\\django code\\bloggingwebsite\\MLBackend\\kidnappingpredictmodel.pickle','rb') as f:
        kidnapping = pickle.load(f)




    dict={'a':"",'revblog':revblog}
    if request.method == "POST":
        try:
            state = request.POST['state']
            states = {
            "AndhraPradesh":1,"ArunachalPradesh":2,"Assam":3,"Bihar":4,"Chhattishgarh":5,"Goa":6,
            "Gujarat":7,"Haryana":8,"HimachalPradesh":9,"JammuandKashmir":10,"Jharkhand":11,"Karnataka":12,
            "Kerala":13,"MadhyaPradesh":14,"Maharashtra":15,"Manipur":16,"Meghalaya":17,"Mizoram":18,
            "Nagaland":19,"Odisha":20,"Punjab":21,"Rajasthan":22,"Sikkim":23,"Tamilnadu":24,
            "Telengana":25,"Tripura":26,"UttarPradesh":27,"Uttarakhand":28,"WestBengal":29,"AndamanNicobar":30,
            "Chandigarh":31,"DamanandDiuandDadraandNagarHaveli":32,"Delhi":33,"Lakshadweep":34,"Puducherry":35,"Ladakh":36,
            }
            year = request.POST['year']
            predictor = request.POST['predictor']
            if predictor=="total":
                a=total.predict([[states[state],year]])
                b="Predicted Crime Rate:"
                c="'static/img/totalcrimepred.jpg'"
            elif predictor=="murder":
                a=murder.predict([[states[state],year]])
                b="Predicted Murder Rate:"
                c="'static/img/murder.jpg'"
            elif predictor=="rape":
                a=rape.predict([[states[state],year]])
                b="Predicted Rape Rate:"
                c="'static/img/rape.jpg'"
            elif predictor=="kidnap":
                a=kidnapping.predict([[states[state],year]])
                b="Predicted Kidnapping Rate:"
                c="'static/img/kidnap.jpg'"

            c=c
            
            dict = {'a':int(a),"b":b,"cardstyle":"background-color:#000000;","divstyle":f"background:url({c}) no-repeat; background-size:cover; height:100vh; opacity: 50%;filter:blur(3px);",
            "class1":"card text-light","class2":"card-img-overlay position-absolute"}
            print(dict)
        
        except:
            dict = {'error':'Select the options appropriately'}
            return render(request,"notfound.html",dict)

        
    return render(request,"crimeprediction.html",dict)