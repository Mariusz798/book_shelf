from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField()
    #book_set
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"