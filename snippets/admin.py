from django.contrib import admin
from .models import Collection, Snippet, Comment, Tag

# Register your models here.

admin.site.register(Collection)
admin.site.register(Snippet)
admin.site.register(Comment)
admin.site.register(Tag)
