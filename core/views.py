from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdminOrReadOnly
from .serializers import *


# Create your views here.

class CurrencyListAPIView(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ('category__name','user__username','currency__code',)
    ordering_fields = ('amount',)

    def get_queryset(self):
        return Transaction.objects.select_related("currency","category","user").filter(user=self.request.user,)

    def get_serializer_class(self):
        if self.action in ("list","retrieve",):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
