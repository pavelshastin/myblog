from django.db import models
from django.conf import settings
from django.utils import timezone

print("models")

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=10)
    n_pingback = models.IntegerField(default=10)
    rating = models.IntegerField()

    def __str__(self):
        return self.headline



