from django.urls import path
from .views import News, Home,  Contact, Signin, addUser

urlpatterns = [
    # Note : Using this name we can do the 'url linking'
    path('', Home, name = 'Home'),
    path('news/', News, name = 'News'),
    path('contact/', Contact, name = 'Contact'),
    path('signin/', Signin, name = 'Signin'),
    path('addUser', addUser, name = 'addUser'),
]