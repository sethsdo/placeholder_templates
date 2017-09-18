from django.shortcuts import render, HttpResponse, redirect         # This line is new!

def register(placeholder):
    placeholder = "register"
    return HttpResponse(placeholder)

def login(placeholder):
    placeholder = "login"
    return HttpResponse(placeholder)


def newUser(param):
    return redirect("/users/register/")

def users(placeholder):
    placeholder = "creates new survey"
    return HttpResponse(placeholder)
