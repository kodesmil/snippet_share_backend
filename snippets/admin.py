from django.contrib import admin

from .models import Collection, Snippet, Tag

# Register your models here.

admin.site.register(Collection)
admin.site.register(Snippet)
admin.site.register(Tag)
