import csv

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from django.core import serializers
from .resources import UsersResources


def user_to_xml(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/xml',
        headers={'Content-Disposition': 'attachment; filename="user_data.xml"'},
    )

    # generate xml_data
    data = serializers.serialize("xml", Users.objects.all(), fields=('first_name', 'last_name'))

    response.write(data)
    return response


def user_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=user_data.csv'

    # create a csv writer
    writer = csv.writer(response)

    users = Users.objects.all()

    # add column headings to csv file
    writer.writerow(['Username', 'Password', 'Date_of_joined'])

    # write content into list
    for user in users:
        writer.writerow([user.username, user.password, user.date_of_join])

    return response


def logout_user(request):
    logout(request)
    messages.success(request, 'You were logout!')
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_list')
        else:
            messages.success(request, 'Yo have failed to login, Try again')
            return redirect('login_user')
    else:
        return render(request, 'user_data/login_user.html', {})


def user_list(request):
    users = Users.objects.all()

    context = {'users': users}
    return render(request, 'user_data/users.html', context)


def home_page(request):
    current_user = request.user
    return render(request, 'user_data/home.html', context={'curr_user': current_user})
