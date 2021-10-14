'''
Urls for shortener app urlshortener/urls.py
'''


from django.urls import path
from .views import create, redirect_url_view
appname = "shortener"


urlpatterns = [
    path('create', create.as_view()),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),


]