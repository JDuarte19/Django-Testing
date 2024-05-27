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
    #extends from base.html
    x = "about.html"
    return render(request, 'user_act/{}'.format(x))

def profile(request):
    #extends base.html
    x = "profile.html"
    return render(request, 'user_act/{}'.format(x))

def admin(request):
    #extends from base.html
    x = "user_table.html"

    accounts = Account.objects.all()
    context = {}
    context['users'] = accounts

    if request.method == "POST":
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            account = Account.objects.get(id=pk)
            if account:
                account.delete()
                context['success'] = True
                return render(request, 'user_act/{}'.format(x),context)
            else:
                context['success'] = False
                return render(request, 'user_act/{}'.format(x),context)

    return render(request, 'user_act/{}'.format(x),context)

def login(request):
    #should be used for token authentication 
    email = request.GET['email']
    password = request.GET['password']
    account = Account.objects.filter(email=email,password=password).values()

def add_account(request):
    #extends from base.html
    #serves as new register page
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            #pass the password to an encryption function
            password = form.cleaned_data['password']
            account = Account(user_name= username, email = email, password = password)
            account.save()
            return render(request, 'user_act/add_account.html', {'form':AccountForm(), 'success':True})
    else:
        form = AccountForm()
        return render(request, 'user_act/add_account.html', {'form':AccountForm()})



def test(request):
    x = "user_table.html"
    #accounts = Account.objects.all()
    context = {}

    #if request.method == "POST":
        #if 'submit' in request.POST:
        #if 'delete' in request.POST:

    
    #context['form'] = form

    return render(request, 'user_act/{}'.format(x),context)