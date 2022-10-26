from django.db import models


class UploadModel(models.Model):
    title = models.CharField('title for upload file', max_length=120)
    file = models.FileField('upload file', null=True)


class Users(models.Model):
    first_name = models.CharField('User first Name', max_length=120)
    last_name = models.CharField('User last Name', max_length=120)
    username = models.CharField('Username', max_length=120, blank=True)
    password = models.CharField('User password', max_length=20, blank=True)
    date_of_join = models.CharField(max_length=100)
    file_input = models.FileField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_data_users"
