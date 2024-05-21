from django.shortcuts import render

# Create your views here.
"""
There are two types of view types.

Function based views

Class based views


"""
# request is the http request a user used to access a webpage
def home(request):
    x = "home.html"
    return render(request, 'user_act/{}'.format(x))

def register(request):
    x = "test.html"
    return render(request, 'user_act/{}'.format(x) )