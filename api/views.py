from django.shortcuts import render, get_object_or_404
from rest_framework import status,views
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError

from ..api.serializers import BookSerializer
from .models import Book

# Create your views here.

class BookCreateAPIView(views.APIView):
    """本モデルの登録APIクラス"""
    def post(self, request, *args, **kwargs):
        """本モデルの登録APIに対応するハンドラメソッド"""

        serializer = BookSerializer(data=request.data)#シリアライザオブジェクトを作成
        serializer.is_valid(raise_exception=True)
        serializer.save() #モデルオブジェクトを登録
        return Response(serializer.data, status.HTTP_201_CREATED)

class BookFilter(filters.FileterSet):
    """本モデル用フィルタクラス"""

    class Meta:
        model = Book
        fields = '__all__'

class BookListAPIView(views.APIView):
    """本モデルの取得(一覧)APIモデル"""
    def get(self, request, *args, **kwargs):
        #モデルオブジェクトをクエリ文字列を使ってフィルタリングした結果を取得
        filterset = BookFilter(request.query_params, queryset=Book.objects.all())
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = BookSerializer(instance=filterset.qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
class BookRetrieveAPIView(views.APIView):
    """本モデルの取得(詳細)APIクラス"""
    def get(self, request, pk, *args, **kwargs):
        """本モデルの取得(詳細)APIに対応するハンドラメソッド"""
        book = get_object_or_404(Book, pk=pk)
        #シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        #レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)
    
class BookUpdateAPIView(views.APIView):
    """本モデルの更新・一部更新APIクラス"""
    def put(self, request, pk, *args, **kwargs):
        """本モデルの更新APIに対応するハンドラメソッド"""
        book = get_object_or_404(Book, pk=pk)#モデルオブジェクトの取得
        serializer = BookSerializer(instance=book, data=request.data)#モデルオブジェクトと入力データを保持したシリアライザオブジェクトを作成
        serializer.is_valid(raise_exception=True)#上で作成したserializerにバリデーションを実行
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request, pk, *args, **kwargs):
        """本モデルの一部更新APIに対応するハンドラメソッド"""
        book = get_object_or_404(Book, pk=pk)#モデルオブジェクトの取得
        #putとの違いはpartial.引数dataで渡した値のみが更新される
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)#上で作成したserializerにバリデーションを実行
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    
class BookDestroyAPIView(views.APIView):
    """本モデルの削除APIクラス"""
    def delete(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)#モデルオブジェクトの取得        
        book.delete() #削除
        return Response(status=status.HTTP_204_NO_CONTENT)
    



