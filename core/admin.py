from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Transaction)