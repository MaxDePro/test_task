import csv, io
import xml

from .forms import UsersForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import re
from .models import *
from django.core import serializers
from .resources import UsersResources


def csv_upload(request):
    template = 'user_data/csv_upload.html'
    prompt = {
        'order': 'Order of csv must contain username, password and join date'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not csv file pick another one')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        (_, created) = Users.objects.update_or_create(
            username=column[0],
            password=column[1],
            date_of_join=column[2]
            )
    context = {}
    return render(request, template, context)


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


def create_user(request):
    submitted = False
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = UsersForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'user_data/create_user.html', context={'form': form, 'submitted': submitted})


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
