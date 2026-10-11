from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, NewsViewSet, StockDataViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'news', NewsViewSet)
router.register(r'stocks', StockDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]