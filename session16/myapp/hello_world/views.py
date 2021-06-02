from hello_world.models import Gretting
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    # CReando un saludo
    greeting = Gretting()
    greeting.heading = "Qué fueeeeeeeee"
    greeting.save()

    #Traer todos los saludos
    greetings = Gretting.objects.all

    # return HttpResponse('Hello world')
    return render(request, 'index.html', {"greetings": greetings})