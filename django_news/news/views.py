import json

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.datetime_safe import datetime
from django.views import View
from django.views.generic import FormView

from .models import News, Message
from django import forms

app_url = "/news/"


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    return render(
        request,
        "index.html",
        {
            "latest_news":
                News.objects.order_by('-pub_date')[:10],
            "message": message
        }
    )


def detail(request, news_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "news.html",
        {
            "a_new": get_object_or_404(
                News, pk=news_id),
            "error_message": error_message,
            "latest_messages":
                Message.objects
                    .filter(chat_id=news_id)
                    .order_by('-pub_date')[:5]
        }
    )


# наше представление для регистрации
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login/"
    template_name = "reg/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    success_url = app_url + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


def post(request, news_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(News, pk=news_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url + str(news_id))


def msg_list(request, news_id):
    res = list(
        Message.objects
            .filter(chat_id=news_id)
            .order_by('-pub_date')[:5]
            .values('author__username',
                    'pub_date',
                    'message'
                    )
    )
    for r in res:
        r['pub_date'] = \
            r['pub_date'].strftime(
                '%d.%m.%Y %H:%M:%S'
            )
    return JsonResponse(json.dumps(res), safe=False)


def admin(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    return render(
        request,
        "admin.html",
        {
            "latest_news":
                News.objects.order_by('-pub_date')[:10],
            "message": message,
        }
    )


def post_news(request):
    author = request.user
    if not (author.is_authenticated and author.is_staff):
        return HttpResponseRedirect(app_url + "admin")

    news = News()
    news.title = request.POST['title']
    news.text = request.POST['text']
    news.pub_date = datetime.now()
    news.save()

    return HttpResponseRedirect(app_url + str(news.id))
