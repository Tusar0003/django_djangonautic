from django.db import models


# Create your models here.
class Article(models.Model):  # inheriting from models.Model

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add will add current time automatically
    # add in thumbnail later
    # add in author later

    def __str__(self):
        return self.title
