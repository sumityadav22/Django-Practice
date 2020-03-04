from django.shortcuts import render
from django.shortcuts import HttpResponse

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