from django.shortcuts import render
from django.http import HttpResponse
from django import forms

import psycopg2
from psycopg2.errors import SerializationFailure

from hello.models import Users

from hello.forms import InputForm

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
   

    return render(request, "index.html")

def success(request):
    return render(request, "success.html")

def submit(request):
    user_info = Users()
    user_info.save()
    user_infos = Users.objects.all()

    context_object_name = 'user_infos'

    return render(request, "submit.html", {"user_infos": user_infos})

def get_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Users() #gets new object
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.major = form.cleaned_data['major']
            obj.age = form.cleaned_data['age']
            obj.gender = form.cleaned_data['gender']
            obj.attractedto = ''.join(form.cleaned_data['attractedTo'])
            obj.distance_campus = form.cleaned_data['distance_from_campus']
            obj.politics = form.cleaned_data['political_beliefs']
            obj.religion = form.cleaned_data['religion']
            obj.sharereligion = form.cleaned_data['do_you_want_someone_who_shares_your_religion']
            obj.drink = form.cleaned_data['do_you_drink']
            obj.social  = form.cleaned_data['time_spent_in_social_activities']
            obj.party  = form.cleaned_data['time_spent_partying_pre_covid']
            #finally save the object in db
            obj.save()
            # redirect to a new URL:
            return render(request, "success.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'submit.html', {'form': form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
