from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(placeholder):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def newform(new):
    return HttpResponse("placeHolder for new form")

def createBlog(new):
    return HttpResponse("placeHolder for new blog")

def number(new, num):
    new = "placeHolder for new blog number" + num
    return HttpResponse(new)


def edit(new, num):
    new = "placeHolder for editing blog number" + num
    return HttpResponse(new)


def delete(new, num):
    new = "placeHolder for deleting blog number" + num
    return HttpResponse(new)

def distroy(new, num):
    return redirect("/blogs/blogs")
