from django.db import models


# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Biography(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    text = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Genre)
    # stack = models.IntegerField()
    # genre = models.IntegerField(choices=Genre)
    # borrowed_by = models.ManyToManyField(User, through='BookRent')

    def __str__(self):
        return f"{self.title}"


# class BookRent(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     from_when = models.DateField(auto_now_add=True)