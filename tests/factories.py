import factory

from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User


class AdminUserFactory(UserFactory):
    is_staff = True
    is_superuser = True
