from django.shortcuts import render, HttpResponse, redirect         # This line is new!


def index(placeholder):
    placeholder = "all surveys created"
    return HttpResponse(placeholder)

def newSurvey(placeholder):
    placeholder = "creates new survey"
    return HttpResponse(placeholder)

