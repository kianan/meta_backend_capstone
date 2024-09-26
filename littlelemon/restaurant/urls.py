from django.urls import path
from . import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # add url path wrt views.py
    path('', views.index, name='index'),
    # path('booking/', BookingView.as_view(), name='booking'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('message/', views.msg),
]
