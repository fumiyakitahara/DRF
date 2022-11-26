from django.contrib import admin
from .models import Book,BookStock,Author,Publisher
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookStock)
admin.site.register(Publisher)