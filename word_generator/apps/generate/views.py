from django.shortcuts import render, HttpResponse, redirect
import random, string
# Create your views here.

def randomword(length):
   return ''.join(random.choice(string.uppercase + string.digits) for i in range(length))

def index(request):
    word = randomword(13)
    stuff = { "wd": word}
    return render(request, 'generate/index.html', stuff)

def create(request):
    # request.session['name'] = request.POST['name']
    # request.session['num'] = 0
    if request.method == "POST":
        if not request.session.has_key('num'):
            request.session['num'] = 1
            print "Getting key"
        else:
            request.session['num'] += 1
            print "Is this working?"
        return redirect('/')
