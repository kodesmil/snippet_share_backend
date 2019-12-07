from django.db import models
from django.contrib.auth.models import User
from snippets.models import Snippet, Comment


class Report(models.Model):
    content = models.CharField(max_length=1000, blank=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
