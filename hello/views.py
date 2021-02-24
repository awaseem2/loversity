import datetime
from datetime import datetime
import math

from django.shortcuts import render
from django.http import HttpResponse
from django import forms

import smtplib
from email.mime.text import MIMEText

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

def meets_requirements(user, form):
    if user.email == None or user.email == form["email"]:
        return False

    # check age
    min_viable_age = math.floor(max(user.age, form["age"]) / 2) + 7
    if min(user.age, form["age"]) < min_viable_age:
        return False

    # check gender
    print(type(user.gender))
    print(type(form["attractedto"]))
    if user.gender not in form["attractedto"]:
        return False

    if form["gender"] not in user.attractedto:
        return False

    if user.religion != form["religion"]:
        if user.sharereligion == "Yes" or form["share_religion"] == "Yes":
            return False

    return True

def get_score_incr(user, form, key):
    if int(getattr(user,key)) - int(form[key]) <= 1:
            return 1 if (int(getattr(user,key)) == int(form[key])) else .5

    return 0

def get_match_compatibility(user, form):
    score = 0

    main_categories = ["distance_campus", "politics", "social", "party"]
    for category in main_categories:
        score += get_score_incr(user, form, category)
    

    # if at least one person has religion as a requirement and they match, (which they will at this point), add 1
    # if religion is a preference of one person and they match, add half a point
    # if neither scare, add 1
    if int(user.sharereligion) == 1 or int(form["share_religion"]) == 1:
        score += 1
    elif int(user.sharereligion) == 2 or int(form["share_religion"]) == 2:
        score += .5 if (user.religion == form["religion"]) else 0
    else:
        score += 1

    # TODO change drink to a choice
    if user.drink == int(form["drink"]):
            score += 1
    
    return score

def get_best_match(form):
    potential = {}
    # accumulate all scores of every user given that they meet requirements
    for user in Users.objects.all():
        if not meets_requirements(user, form):
            continue

        score = get_match_compatibility(user, form)
        potential[user] = score

    # find the highest score
    # TODO: incorporate pastmatches column (add to it and check if there)
    best_match_info = ('', -1)
    for match in potential.keys():
        if potential[match] > best_match_info[1]:
            best_match_info = (match, potential[match])
    
    best_match = best_match_info[0]
    user_info = {}
    if best_match == '':
        return user_info

    user_info['name'] = best_match.name
    user_info['email'] = best_match.email
    user_info['major'] = best_match.major
    user_info['age'] = best_match.age

    return user_info

def save_form(form):
    obj = Users() #gets new object
    obj.name = form['name']
    obj.email = form['email']
    obj.major = form['major']
    obj.age = form['age']
    obj.gender = form['gender']
    obj.attractedto = form['attractedto']
    obj.distance_campus = form['distance_campus']
    obj.politics = form['politics']
    obj.religion = form['religion']
    obj.sharereligion = form['sharereligion']
    obj.drink = form['drink']
    obj.social  = form['social']
    obj.party  = form['party']
    #finally save the object in db
    obj.save()

def submit(request):
    user_info = Users()
    user_info.save()
    user_infos = Users.objects.all()

    context_object_name = 'user_infos'

    

def get_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_form = {}
            cleaned_form['name'] = form.cleaned_data['name']
            cleaned_form['email'] = form.cleaned_data['email']
            cleaned_form['major'] = form.cleaned_data['major']
            cleaned_form['age'] = form.cleaned_data['age']
            cleaned_form['gender'] = form.cleaned_data['gender']
            cleaned_form['attractedto'] = ''.join(form.cleaned_data['attracted_to'])
            cleaned_form['distance_campus'] = form.cleaned_data['distance_from_campus']
            cleaned_form['politics'] = form.cleaned_data['political_beliefs']
            cleaned_form['religion'] = form.cleaned_data['religion']
            cleaned_form['sharereligion'] = form.cleaned_data['do_you_want_someone_who_shares_your_religion']
            cleaned_form['drink'] = form.cleaned_data['do_you_drink']
            cleaned_form['social'] = form.cleaned_data['time_spent_in_social_activities']
            cleaned_form['party'] = form.cleaned_data['time_spent_partying_pre_covid']

            save_form(cleaned_form)

            # redirect to a new URL:
            #request.POST = request.GET.POST()
            user_info = get_best_match(cleaned_form)
            if len(user_info) != 0:
                return render(request, "success.html", {"user_info": user_info})

            return render(request, "successEmpty.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'submit.html', {'form': form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})