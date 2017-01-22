from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
            'img': "No ninjas to see here, GET OUT"
    }
    return render(request, 'disninja/index.html', context)


def appear(request):
    context = {
            'img': "Wazzaaaa"
    }
    return render(request, 'disninja/index.html', context)

def ninjatime(request, color):
    if color == 'orange':
        context = {
            'img': "/disninja/cutem.png"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "blue":
        context = {
                'img': "JAMES"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "red":
        context = {
                'img': "JAMES"
        }
        return render(request, 'disninja/index.html', context)
    elif color == "purple":
        context = {
                'img': "JAMES"
        }
        return render(request, 'disninja/index.html', context)
