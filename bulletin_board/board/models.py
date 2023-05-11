from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Smiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potionbrewers', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний')
    ]

    title = models.CharField(max_length=254)
    body = models.TextField()
    category = models.CharField(max_length=254, choices=CATEGORY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Response(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
