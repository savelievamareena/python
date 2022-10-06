from django.urls import path, re_path
from . import views

app_name = 'riddles'

urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
    re_path(r'^register/$', views.RegisterFormView.as_view()),
    re_path(r'^login/$', views.LoginFormView.as_view()),
    re_path(r'^logout/$', views.LogoutView.as_view()),
    re_path(r'^password-change/', views.PasswordChangeView.as_view()),
    re_path(r'^([0-9]+)/post/$', views.post, name='post'),
    re_path(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
    re_path(r'^([0-9]+)/post/$', views.post, name='post'),
    re_path(r'^admin/$', views.admin, name='admin'),
    re_path(r'^post_news/$', views.post_news, name='post_news'),
]
