from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    print courses
    return render(request, 'courseapp/index.html', context)

def addition(request):
    Course.objects.create(course=request.POST['name'], description=request.POST['desc'])
    messages.warning(request, 'Success!')
    return redirect('/')

def destroy(request, jim):
    jimbo = Course.objects.filter(id=jim)
    context = {
            'jimbo': jimbo
    }
    return render(request, 'courseapp/remove.html', context)

def demolish(request, jim):
    sucker = Course.objects.filter(id=jim).delete()
    context = {
            'sucker': sucker
    }
    return redirect('/', context)
