# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import django.contrib.sessions.backends.cache
# from django.contrib.models import session



# Create your views here.
def index(request):
    context = { }
    return render (request, "SurveyForm_app/survey.html", context)

def process(request):
    request.session['yourName'] = request.POST['yourName']
    request.session['dojo'] = request.POST['dojoLocation']
    request.session['favLang'] = request.POST['favLanguage']
    request.session['comment'] = request.POST['comment']

    try:
        request.session['counter'] = request.session['counter'] + 1;
    except Exception as e:
        request.session['counter'] = 1;
    print "request.POST['yourName'] = ", request.POST['yourName']
    print "request.session['yourName']", request.session['yourName']

    # if the conent are not invalid, redirect to survey.
    # else open result
    # return render (request, "SurveyForm_app/result.html", context)
    return render (request, "SurveyForm_app/result.html")
    # return redirect("/result")

def result(request):
    return render (request, "SurveyForm_app/result.html")
