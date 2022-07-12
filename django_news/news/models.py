from django.db import models


class Title(models.Model):
    title_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class NewsBody(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField(blank=False)