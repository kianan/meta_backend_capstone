from django.urls import path
from . import views

urlpatterns = [
    # add url path wrt views.py
    path('', views.index, name='index')
]
