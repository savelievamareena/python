from django.urls import path, re_path
from . import views

app_name = 'riddles'

urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
]
