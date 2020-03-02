from django.urls import path
from .views import News

urlpatterns = [
    path('news/', News, name = 'News'),
]