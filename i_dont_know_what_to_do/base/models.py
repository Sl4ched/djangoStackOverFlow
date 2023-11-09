from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.quantity


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.myuser.save()


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
    user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)

    discuss = models.ForeignKey(Discuss, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=200, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
