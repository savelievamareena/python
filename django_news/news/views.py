from django.shortcuts import get_object_or_404, render, redirect
from .models import Title, NewsBody


# главная страница со списком заголовков
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "index.html",
        {
            "latest_titles":
                Title.objects.order_by('-pub_date')[:5],
            "message": message
        }
    )


#страница с новостью целиком
def detail(request, title_id):
    error_message = None
    title = get_object_or_404(Title, pk=title_id)
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "news.html",
        {
            "title": get_object_or_404(Title, pk=title_id),
            "error_message": error_message
        }
    )
