import uuid
from django.db import models

# Create your models here.
class Author(models.Model):
    """著者モデル"""
    class Meta:
        db_table = 'author'
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='著者名', max_length=20)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

class Publisher(models.Model):
    """出版社モデル"""
    class Meta:
        db_table = 'publisher'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='出版社名', max_length=20)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)



class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'
        ordering = ['created_at']
        verbose_name = verbose_name_plural = '本' #管理場面の表示名が変わる

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    author = models.ManyToManyField(Author, verbose_name='著書', blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.PROTECT,null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title

class BookStock(models.Model):
    """本の在庫モデル"""

    class Meta:
        db_table = 'book_stock'

    book = models.OneToOneField(Book, verbose_name='本',on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数',default=0)