import io,urllib,base64
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.shortcuts import render,HttpResponse
from home.models import Blog
revblog = Blog.objects.filter().order_by('-sno')[:4:1]

def Graph(request):
    df=pd.read_excel("D:\CODE\ML project\Graph_crimes_data.xlsx", index_col='State')
    States =[str(_) for _ in df.index]
    Crimes = df['Crimes_2019']

    # now
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    explode = []
    for i in range(0,12):
        explode.append(0.1)

    print(len(explode))
    
    if request.method == "POST":
        a = request.POST['language']
        a = int(a)
        print(a)

        b = request.POST['page']
        b = int(b)
        print(b)

        def creategraph():
            ax,fig = plt.subplots(figsize=(12,8))
            plt.subplots_adjust(bottom=0.1,right=0.8)
            pieStates = []
            pieCrimes = []
            if b==2:
                for i in range(12,24):
                    pieStates.append(States[i])
                    pieCrimes.append(Crimes[i])
                wedges,texts,autotexts=plt.pie(pieCrimes,labels=pieStates,autopct = lambda pct: func(pct, pieCrimes),startangle = 90,wedgeprops = wp,textprops = {'color':"magenta"},explode=explode)
                fig.legend(wedges, pieStates,title ="States",loc ="center left",bbox_to_anchor =(1, 0.1, 0.5, 1))
                fig = plt.gcf()
            elif b==3:
                for i in range(24,36):
                    pieStates.append(States[i])
                    pieCrimes.append(Crimes[i])
                wedges,texts,autotexts=plt.pie(pieCrimes,labels=pieStates,autopct = lambda pct: func(pct, pieCrimes),startangle = 90,wedgeprops = wp,textprops = {'color':"magenta"},explode=explode)
                fig.legend(wedges, pieStates,title ="States",loc ="center left",bbox_to_anchor =(1, 0.1, 0.5, 1))
                fig = plt.gcf()
            else:
                for i in range(0,12):
                    pieStates.append(States[i])
                    pieCrimes.append(Crimes[i])
                wedges,texts,autotexts=plt.pie(pieCrimes,labels=pieStates,autopct = lambda pct: func(pct, pieCrimes),startangle = 90,wedgeprops = wp,textprops = {'color':"magenta"},explode=explode)
                fig.legend(wedges, pieStates,title ="States",loc ="center left",bbox_to_anchor =(1, 0.1, 0.5, 1))
                fig = plt.gcf()
            buf = io.BytesIO()
            fig.savefig(buf,format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri=urllib.parse.quote(string)
            dict = {'plot':uri,'a':a,'b':b,'hidden':f'<img src="data:image/png;base64,{uri}" class="border border-3 border-warning shadow-lg"></img>','revblog':revblog}
            return dict
        

        if a == 2008:
            Crimes=df['Crimes_2008']
            dict=creategraph()

        elif a == 2009:
            Crimes=df['Crimes_2009']
            dict=creategraph()

        elif a == 2010:
            Crimes=df['Crimes_2010']
            dict=creategraph()

        elif a == 2011:
            Crimes=df['Crimes_2011']
            dict=creategraph()

        elif a == 2012:
            Crimes=df['Crimes_2012']
            dict=creategraph()
        
        elif a == 2013:
            Crimes=df['Crimes_2013']
            dict=creategraph()

        elif a == 2014:
            Crimes=df['Crimes_2014']
            dict=creategraph()

        elif a == 2015:
            Crimes=df['Crimes_2015']
            dict=creategraph()

        elif a == 2016:
            Crimes=df['Crimes_2016']
            dict=creategraph()

        elif a == 2017:
            Crimes=df['Crimes_2017']
            dict=creategraph()

        elif a == 2018:
            Crimes=df['Crimes_2018']
            dict=creategraph()

        elif a == 2019:
            Crimes=df['Crimes_2019']
            dict=creategraph()

        
        else:
            dict = {'plot':'none',
        'a':'none',
        'b':'none',
        'hidden':'',
        'revblog':revblog
        }
    
    else:
        dict = {'plot':'none',
        'a':'none',
        'b':'none',
        'hidden':'',
        'revblog':revblog
        }
        

    return render(request,'graph.html',dict)
