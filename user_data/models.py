from django.db import models


class Users(models.Model):
    first_name = models.CharField('User first Name', max_length=120, blank=True)
    last_name = models.CharField('User last Name', max_length=120, blank=True)
    username = models.CharField('Username', max_length=120, blank=True)
    password = models.CharField('User password', max_length=20, blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    # class Meta:
    #     db_table = "user_data_users"
