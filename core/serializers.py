from rest_framework import serializers

from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("code", "name",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = (fields,)


class WriteTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = "__all__"
