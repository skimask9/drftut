from email.policy import default
from .models import *
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    user = serializers.SlugRelatedField(slug_field= "username", queryset = User.objects.all())
    category = serializers.SlugRelatedField(slug_field= "name",queryset = Category.objects.all())
    class Meta:
        model = Transaction
        fields = "__all__" 
        read_only_fields = (fields,)

class WriteTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field = "code", queryset = Currency.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(slug_field= "name", queryset = Category.objects.all())
    class Meta:
        model = Transaction
        fields = "__all__" 