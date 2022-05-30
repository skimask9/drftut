from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet)
router.register(r'transactions', views.TransactionModelViewSet, basename='transactions')
router.register(r'currencies', views.CurrencyListAPIView, basename='currencies')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    # path('currencies/', views.CurrencyListAPIView.as_view()),
    path('login/', obtain_auth_token),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('categories/', views.CategoryModelViewSet.as_view())
]+ router.urls
    