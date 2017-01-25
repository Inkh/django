from django.shortcuts import render, redirect
import re
import md5
import bcrypt
from django.contrib import messages
from .models import User
# Create your views here.
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

def index(request):
    if request.session.has_key('id'):
        return redirect('/success/' + str(request.session['id']))
    return render(request, 'logreg/index.html')


def register(request):
    checker = User.objects.all()
    first_name = request.POST['first_name'].lower()
    last_name = request.POST['last_name'].lower()
    email = request.POST['email'].lower()
    pw_1 = request.POST['pw_1'].encode()
    pw_2 = request.POST['pw_2'].encode()
    pw_hash = bcrypt.hashpw(pw_1, bcrypt.gensalt())
    validate = True

    for x in checker:
        if x.email == email:
            validate = False
            messages.warning(request, "That email already exists!")
            break
    if len(first_name) < 1:
        messages.warning(request, "First Name must not be empty!")
        validate = False
    if len(last_name) < 1:
        messages.warning(request, "Last Name must not be empty!")
        validate = False
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        messages.warning(request, "Email not valid!")
        validate = False
    if len(pw_1) < 8 or len(pw_2) < 8:
        messages.warning(request, "Password fields must be longer than 8 characters!")
        validate = False
    if pw_1 != pw_2:
        messages.warning(request, "Passwords do not match!")
        validate = False
    if not first_name.isalpha() or not last_name.isalpha():
        messages.warning(request, "Name Field must be letters!")
        validate = False
    if request.session.has_key('id'):
        print request.session['id']
    if validate:
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email,password=pw_hash)
        request.session['id'] = user.id
        print request.session['id']
        print "Success"
        return redirect('/success/' + str(user.id))
    else:
        return redirect('/')


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
    return render(request, 'logreg/logged.html', context)


def logout(request):
    request.session.pop('id')
    return redirect('/')

def login(request):
    email = request.POST['email']
    pw = request.POST['pw_1'].encode()
    user_list = User.objects.filter(email=email)
    validate = True
    if not user_list:
        validate = False
        messages.warning(request, "Email doesn't exist, please try again.")
        return redirect('/')
    else:
        if not bcrypt.hashpw(pw, user_list[0].password.encode()) == user_list[0].password.encode():
            validate = False
            messages.warning(request, "Password does not match, please try again.")
    if validate:
        user_id = user_list[0].id
        request.session['id'] = user_id
        print user_id
        print "you did it"
        return redirect('/success/' + str(user_id) )
    else:
        return redirect('/')


def nein(request, word):
    messages.warning(request, "DON'T GO TO PLACES THAT DO NOT EXIST. IT'S DANGEROUS! 404! 404!")
    return redirect('/')
