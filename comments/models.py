from django.contrib.auth.models import User
from django.db import models

from snippets.models import Snippet


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, related_name='comments', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=0)
