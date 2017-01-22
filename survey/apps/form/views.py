from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'form/index.html')

def process(request):
    if not request.session.has_key('num'):
        request.session['num'] = 1
    else:
        request.session['num'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['lang'] = request.POST['lang']

    return redirect('/moja')

def moja(request):

    return render(request, 'form/moja.html')
    
