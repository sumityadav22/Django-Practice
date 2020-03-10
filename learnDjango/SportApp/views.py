from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .forms import RegistrationForm, RegistrationModal
from .models import RegistrationData
from django.contrib import messages

# Create your views here.

def Home(request):
    context = {
        'name':'Sumit Yadav',
        'phone_number':8286828682
    }
    return render(request,'home.html', context)

def News(request):
    context = {
        "news_list": ["Sports", "Political", "Entertainment", "Bollywood", "Hollywood"]
    }
    return render(request,'news.html',context)

def Contact(request):
    context = {
        "age": 20
    }
    return render(request,'contact.html',context)

def Signin(request):
    context = {
        "form":RegistrationForm
    }
    return render(request,'signin.html',context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
        password = form.cleaned_data['password'],
        email = form.cleaned_data['email'],
        phone = form.cleaned_data['phone'])

        myregister.save()
        messages.add_message(request, messages.SUCCESS, "You have signed up successfuly")

    return redirect('Signin')

def modalFrom(request):
    context = {
        'modalform':RegistrationModal
    }
    return render(request,'modalForm.html', context)


def addModalForm(request):
    mymodalform = RegistrationModal(request.POST)

    if mymodalform.is_valid():
        mymodalform.save()
        
    return redirect('modalForm')