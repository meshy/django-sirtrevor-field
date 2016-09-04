from django.db import models

from sirtrevor.modelfields import SirTrevorField


class Post(models.Model):
    content = SirTrevorField(default='')
