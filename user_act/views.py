from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import AccountForm
from .models import Account

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

def about(request):
    x = "about.html"
    return render(request, 'user_act/{}'.format(x))

def login(request):
    #should be used for token authentication 
    email = request.GET['email']
    password = request.GET['password']
    account = Account.objects.filter(email=email,password=password).values()

def register(request):
    x = "register.html"
    return render(request, 'user_act/{}'.format(x))

def reg_account(request):
    username = request.POST['username']
    email = request.POST['email']
    #pass the password to an encryption function
    password = request.POST['password']
    account = Account(user_name= username, email = email, password = password)
    account.save()
    return HttpResponseRedirect(reverse('home'))

def test(request):
    x = "test.html"
    accounts = Account.objects.all()
    context = {}
    form = AccountForm()
    context['users'] = accounts

    if request.method == "POST":
        if 'submit' in request.POST:
            form = AccountForm(request.POST)
            form.save()
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            accounts = Account.objects.get(id=pk)
            accounts.delete()
    
    context['form'] = form

    return render(request, 'user_act/{}'.format(x),context)