from rest_framework import serializers
from .models import Book
import random
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    本モデルのシリアライザ　ModelSerializer編
    JSONの出入力がモデルのフィールド定義がもとになる場合に使う   
    """
    class Meta:
        model = Book #対象モデルの指定
        fields = ['id','title','price'] #利用するモデルのフィールド,全て指定したい場合は"__all__""

class BookListSerializer(serializers.ListSerializer):
    """
    複数の本もでるを扱うためのシリアライザ
    一覧取得APIや関連先のモデルを参照するため
    """
    child = BookSerializer()#対象のシリアライザを指定

class FortuneSerializer(serializers.Serializer):
    """
    今日の運勢を返すシリアライザ
    モデルに依存しない自由な形式JSONを入出力するAPIを作成したい場合
    """
    birth_date = serializers.DateField()
    blood_type = serializers.CharField(choices = ["A","B","O","AB"])
    current_date = serializers.SerializerMethodField()
    fortune = serializers.SerializerMethodField()

    def get_current_date(self,obj):
        return timezone.localdate()

    def get_fortune(self,obj):
        seed = '{}{}{}'.format(timezone.localdate(),obj['birth_date'],obj['blood_type'])
        random.seed(seed)
        return random.choice(
            ['★☆☆☆☆','★★☆☆☆','★★★☆☆','★★★★☆','★★★★★']
            )