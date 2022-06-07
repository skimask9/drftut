from django.shortcuts import render
import requests
from core.models import Transaction
from django.db.models import Sum, Avg, Count, Max, Min, Q


# Create your views here.


def index(request):
    url = 'http://127.0.0.1:8000/transactions/'
    token = 'Token 2381021c1b8712554a71ddbf2bfa590a8f11028c'  # user api-token
    headers = {
        'Authorization': token
    }
    r = requests.get(url, headers=headers).json()

    total = Transaction.objects.values("category__name", "currency__code").annotate(
        total=Sum("amount"),
        count=Count("id"),
        avg=Avg("amount")
    )
    total_by_user = Transaction.objects.values("user__username",
                                               "category__name",
                                               "currency__code").annotate(
        total=Sum("amount"),
        count=Count("id"),
        max=Max("amount"),
        min=Min("amount")
    )
    queryset = Transaction.objects.filter(Q(amount__range=(125, 132)) | Q(amount__range=(250, 500)))
    data = []
    for s in r:
        data.append(s)
    return render(request, "core_response/home.html",
                  {
                      "data": data,
                      # "datacur":datacur,
                      "total": total,
                      "total_by_user": total_by_user,
                      "queryset": queryset
                  })
