from django.urls import path
from .views import News, Home,  Contact

urlpatterns = [
    # Note : Using this name we can do the 'url linking'
    path('', Home, name = 'Home'),
    path('news/', News, name = 'News'),
    path('contact/', Contact, name = 'Contact'),
]