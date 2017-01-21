from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    t = datetime.datetime.now()
    d = datetime.datetime.today()
    time = ("%s/%s/%s/%s.%s.%s"%(t.month,t.day,t.year,t.hour,t.minute,t.second))

    bullhonkey = {
        "james": time,
        "realtime": d
    }
    return render(request, 'timedisplay/index.html', bullhonkey)
