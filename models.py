from django.db import models


# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg', upload_to='book_images/')
# forms
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','desc','book_image','price']
# admin
from django.contrib import admin
from .models import Book
# Register your models here.

admin.site.register(Book)
