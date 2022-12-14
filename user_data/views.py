import csv, io

from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core import serializers

import re
from .serializers import parse_xml_data


# Creating a page to upload xml file with users data
def xml_upload(request):
    if request.method == 'POST':
        form = UploadModelForm(request.POST, request.FILES)
        # if form.is_valid():
        users_data = parse_xml_data(request.FILES['xml_file'])
        for person_id in users_data:
            (_, created) = Users.objects.update_or_create(
                first_name=re.sub('\(.*?\)', '', users_data.get(person_id).get('first_name')),
                last_name=re.sub('\(.*?\)', '', users_data.get(person_id).get('last_name')),
            )
        return redirect('home')
    else:
        form = UploadModelForm()
    return render(request, 'user_data/xml_upload.html', {'form': form})


# def xml_upload_2(request):
#     xml_file_2 = request.FILES['xml_file_2']
#     users_data = parse_xml_data(xml_file_2)
#     for person_id in users_data:
#         (_, created) = Users.objects.update_or_create(
#             first_name=users_data.get(person_id).get('first_name'),
#             password=users_data.get(person_id).get('last_name'),
#         )
#     return render(request, 'user_data/xml_upload_2.html', {})


# Creating a page to upload csv file with users data
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
        if column[0] and column[1] and column[2]:
            if column[0].find('(') >= 1 or column[0].find('[') >= 1:
                column[0] = re.sub('\(.*?\)', '', column[0])
            (_, created) = Users.objects.update_or_create(
                username=column[0],
                password=column[1],
                date_of_join=column[2]
                )
    context = {}
    return render(request, template, context)


# Creating a page to download xml file with users data
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


# Creating a page to download csv file with users data
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


# Creating a page clicking to username of user in user list we get detail info about user
def user_detail(request, user_id):
    user = Users.objects.get(pk=user_id)
    context = {
        'usr': user
    }
    return render(request, 'user_data/user_detail.html', context)


# Creating a page to create new users
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


# Creating a page to logout user
def logout_user(request):
    logout(request)
    messages.success(request, 'You were logout!')
    return redirect('home')


# Creating a page to login user
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


# Creating a page to register new users
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You success registrated')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'user_data/register_user.html', context={'form': form})


# Creating view of list of all users
def user_list(request):
    users = Users.objects.all()

    context = {'users': users}
    return render(request, 'user_data/users.html', context)

# Creating view of homepage
def home_page(request):
    current_user = request.user
    return render(request, 'user_data/home.html', context={'curr_user': current_user})
