from django.db.models import Sum,Avg,Count

from core.models import Transaction


def transaction_report():
    queryset = Transaction.objects.values("category__name").annotate(
        total = Sum("amount"),
        count = Count("id"),
        avg = Avg("amount")
    )

    return queryset