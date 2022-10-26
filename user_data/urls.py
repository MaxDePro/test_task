from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('user_list', user_list, name='user_list'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),
    path('user_to_csv', user_to_csv, name='user_to_csv'),
    path('user_to_xml', user_to_xml, name='user_to_xml'),
    path('csv_file', csv_upload, name='csv_file'),
    # path('xml_file', xml_upload, name='xml_file'),
    path('create_user', create_user, name='create_user'),
    path('register_user', register_user, name='register_user'),
    path('user_detail/<user_id>', user_detail, name='user_detail'),
]
