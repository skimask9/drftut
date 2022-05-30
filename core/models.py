from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,related_name="transactions")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User")
    category = models.ForeignKey(
        Category,on_delete=models.SET_NULL,default=1,null=True,blank=True,related_name="transactions"
    )

    def __str__(self) -> str:
        return f"{self.amount} == {self.currency} by {self.user} at {self.date}"
