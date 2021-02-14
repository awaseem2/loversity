from django.shortcuts import render
from django.http import HttpResponse
from django import forms

import psycopg2
from psycopg2.errors import SerializationFailure

from hello.models import Users

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
   

    return render(request, "index.html")

def submit(request):
    user_info = Users()
    user_info.save()
    user_infos = Users.objects.all()

    context_object_name = 'user_infos'

    return render(request, "submit.html", {"user_infos": user_infos})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
