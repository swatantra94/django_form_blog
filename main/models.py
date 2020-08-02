from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title