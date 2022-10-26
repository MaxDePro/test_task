from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('user_list', user_list, name='user_list'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),
    path('user_to_csv', user_to_csv, name='user_to_csv'),
    path('user_to_xml', user_to_xml, name='user_to_xml'),
]
