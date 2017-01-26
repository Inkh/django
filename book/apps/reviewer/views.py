from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review, Author, Registration, Login
#TODO REMOVE AFTER TESTING
import bcrypt
import md5
# Create your views here.

def index(request):
    if request.session.has_key('id'):
        return redirect('/success/' + str(request.session['id']))
    return render(request, 'reviewer/index.html')


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
    return render(request, 'reviewer/logged.html', context)

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

def addreview(request, id):
    title = request.POST['title']
    book_list = Book.objects.filter(title=title)
    if not book_title:
        book_title = Book.objects.create(title=title)
    else:
        book_title = book_list[0]

    name = request.POST['name']

    author_list = Author.objects.filter(name=name)
    if not author_list:
        author_name = Author.objects.create(name=name)
    else:
        author_name = author_list[0]

    book_review = request.POST['text']
    id = request.session['id']
    user = User.objects.filter(id=id)
    context = {
            'users': user,
            'link_id': id
    }
    return render(request, 'reviewer/add.html', context)





# ****** TRASH ******

    # pw_hash = bcrypt.hashpw(pw_1, bcrypt.gensalt())
    # try to move
    # for x in checker:
    #     if x.email == email:
    #         validate = False
    #         messages.warning(request, "That email already exists!")
    #         break
    # if len(first_name) < 1:
    #     messages.warning(request, "First Name must not be empty!")
    #     validate = False
    # if len(last_name) < 1:
    #     messages.warning(request, "Last Name must not be empty!")
    #     validate = False
    # if len(email) < 1 or not EMAIL_REGEX.match(email):
    #     messages.warning(request, "Email not valid!")
    #     validate = False
    # if len(pw_1) < 8 or len(pw_2) < 8:
    #     messages.warning(request, "Password fields must be longer than 8 characters!")
    #     validate = False
    # if pw_1 != pw_2:
    #     messages.warning(request, "Passwords do not match!")
    #     validate = False
    # if not first_name.isalpha() or not last_name.isalpha():
    #     messages.warning(request, "Name Field must be letters!")
    #     validate = False
# TODO UNCOMMENT BELOW AFTER TESTING
#
# if request.session.has_key('id'):
#     print request.session['id']
#     return redirect('/success/' + str(user.id))

# ******ORIGINAL UNFACTORED LOGIN CODE******

# email = request.POST['email']
# pw = request.POST['pw_1'].encode()
# user_list = User.objects.filter(email=email)
# validate = True
# if not user_list:
#     validate = False
#     messages.warning(request, "Email doesn't exist, please try again.")
#     return redirect('/')
# else:
#     if not bcrypt.hashpw(pw, user_list[0].password.encode()) == user_list[0].password.encode():
#         validate = False
#         messages.warning(request, "Password does not match, please try again.")
# if validate:
#     user_id = user_list[0].id
#     request.session['id'] = user_id
#     print user_id
#     print "you did it"
#     return redirect('/success/' + str(user_id) )
# else:
#     return redirect('/')
