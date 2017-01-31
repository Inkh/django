from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote, Registration, Login
#TODO REMOVE AFTER TESTING
import bcrypt
import md5
# Create your views here.
def index(request):
    if request.session.has_key('id'):
        return redirect('/success/' + str(request.session['id']))
    return render(request, 'belter/index.html')


def register(request):
    if request.method == 'POST':
        newuser = Registration()
        newuser.first_name = request.POST['first_name'].lower()
        newuser.last_name = request.POST['last_name'].lower()
        newuser.email = request.POST['email'].lower()
        newuser.pw_1 = request.POST['pw_1'].encode()
        newuser.pw_2 = request.POST['pw_2'].encode()
        newuser.validate()
        for x in newuser.message:
            messages.warning(request, x)
        if newuser.is_valid:
            newuser.create_user()
            request.session['id'] = newuser.id
            return redirect('success/{}'.format(request.session['id']))
        else:
            return redirect('/')
    else:
        return redirect('/')
        # try to move


def success(request, id):
    if not request.session.has_key('id'):
        messages.warning(request, "DON'T YOU TAMPER WITH ME MAN")
        return redirect('/')
    print request.session['id']
    id = request.session['id']
    user = User.objects.filter(id=id)
    context = {
            'users':user
    }
    return render(request, 'belter/logged.html', context)

def login(request):
    userlog = Login()
    userlog.email = request.POST['email']
    userlog.pw = request.POST['pw_1'].encode()
    userlog.validation()
    for x in userlog.message:
        messages.warning(request, x)
    if userlog.validate:
        request.session['id'] = userlog.id
        return redirect('/success/{}'.format(request.session['id']))
    else:
        return redirect('/')


def logout(request):
    request.session.pop('id')
    return redirect('/')

def account(request):
    return redirect('/')

def nein(request, word):
    messages.warning(request, "DON'T GO TO PLACES THAT DO NOT EXIST. IT'S DANGEROUS! 404! 404!")
    return redirect('/')
