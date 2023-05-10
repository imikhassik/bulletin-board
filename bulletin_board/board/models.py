from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=254)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Attachment(models.Model):
    name = models.CharField(max_length=254)
    file = models.FileField(upload_to='attachments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Category(models.Model):
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
    name = models.CharField(max_length=254, choices=CATEGORY_CHOICES)


class Response(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
