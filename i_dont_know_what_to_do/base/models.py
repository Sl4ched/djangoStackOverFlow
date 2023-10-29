from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tags = models.CharField(max_length=50, null=True)
    tag_body = models.TextField(null=True, blank=True)
    tag_count = models.IntegerField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tags


class Discuss(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    topics = models.ManyToManyField(Tag, related_name='topics')
    views = models.ManyToManyField(User, related_name='user')

    title = models.CharField(max_length=300)
    body = models.TextField()

    votes = models.IntegerField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:60] + "..."


class Answer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    discuss = models.ForeignKey(Discuss, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=200, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
