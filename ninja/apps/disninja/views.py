from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
            'msg':  "Nothing to see here.. Get out.. GET OUT!"
    }
    return render(request, 'disninja/index.html', context)


def appear(request):
    context = {
            'img': "/disninja/TMNT.jpg"
    }
    return render(request, 'disninja/index.html', context)

def ninjatime(request, color):
    if color == 'orange':
        context = {
            'img': "/disninja/cutem.png"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "purple":
        context = {
                'img': "/disninja/dona.jpg"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "red":
        context = {
                'img': "/disninja/raphael.jpg"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "blue":
        context = {
                'img': "/disninja/leo.jpg"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "pizza":
        context = {
        'msg': "YOU'RE SUPPOSED TO ENTER A COLOR!! WHY, OH GOD WHY YOU GOTTA FEED'EM PIZZA, WHO'S GONNA PROTECT US FOR THE NEXT 4 HOURS!?",
        'img': "/disninja/tmntpizza.jpg"
        }
        return render(request, 'disninja/index.html', context)
