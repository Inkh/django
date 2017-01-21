from django.shortcuts import render, HttpResponse

def index(request):
    print "Hello, I am Doge!"
    return render(request, "first_app/index.html")

def show(request):
    print "Showing!"
    return render(request, "first_app/users.html")
# Create your views here.
