from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'password', 'date_of_join')
