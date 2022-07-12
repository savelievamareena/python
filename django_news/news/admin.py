from django.contrib import admin

from .models import Title, NewsBody

admin.site.register(Title)
admin.site.register(NewsBody)