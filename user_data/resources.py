from import_export import resources
from .models import Users


class UsersResources(resources.ModelResource):
    class Meta:
        model = Users
