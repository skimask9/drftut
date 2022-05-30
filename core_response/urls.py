from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path("response/",views.index, name="main"),
]
