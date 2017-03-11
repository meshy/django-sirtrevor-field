import factory

from django.contrib.auth.models import User

from .models import Post


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('user{}'.format)

    class Meta:
        model = User


class AdminUserFactory(UserFactory):
    is_staff = True
    is_superuser = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        assert create

        if extracted is None:
            extracted = 'default_password'
        self.raw_password = extracted
        self.set_password(extracted)
        self.save()


class PostFactory(factory.DjangoModelFactory):
    content = factory.LazyAttribute(lambda o: {})

    class Meta:
        model = Post
