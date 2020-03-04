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
    return render(request,'news.html')

def Contact(request):
    return render(request,'contact.html')