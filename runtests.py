#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691."""
import os
import sys

import dj_database_url
import django
from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings
from django.test.runner import DiscoverRunner


settings.configure(
    DATABASES={'default': dj_database_url.config(
        default='postgres:///sirtrevor',
    )},
    INSTALLED_APPS=(
        'tests',
        'django.contrib.admin',
        # contenttypes must preceed auth: http://stackoverflow.com/a/18292090/400691
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    OVERWRITE_SCREENSHOTS=os.environ.get('OVERWRITE_SCREENSHOTS', False),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher',),
    ROOT_URLCONF='tests.urls',
    STATIC_URL='/static/',
    TEMPLATES=[{
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    }],
)


django.setup()


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    """Enable coloured output for tests."""


test_runner = TestRunner(verbosity=2)
failures = test_runner.run_tests(None)
if failures:
    sys.exit(1)
