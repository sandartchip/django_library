from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='enter a book Genre')

    def __str__(self):
        "string for representing the model object"
        return self.name

class Book(models.Model): #제목, 작가, 요약, isbn, 장르

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET)

    summary = models.TextField(max_length=1000, help_text='enter a brief description')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 character <a href='https://www.isbn)


#class BookInstance(models.Model): # 누군가 빌릴지도 모를 특정한 책의 복사본.
#    id = models.UUIDField()