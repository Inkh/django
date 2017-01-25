from django.shortcuts import render, redirect
import re
from .models import Email
from django.contrib import messages
# Create your views here.
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


def index(request):
    emails = Email.objects.all()
    context = {
        'emails':emails
    }
    return render(request, 'emailval/index.html', context)


def add(request):
    if EMAIL_REGEX.match(request.POST['email']):
        messages.warning(request, "Success! " + request.POST['email'] + " is a valid email address!")
        Email.objects.create(address=request.POST['email'])
        return redirect('/')
    else:
        messages.warning(request, "You did not enter a valid email address!")
        return redirect('/')


def destroy(request):
    return redirect('/')
