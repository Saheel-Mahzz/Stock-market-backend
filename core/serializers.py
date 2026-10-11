from rest_framework import serializers
from .models import Company, News, StockData

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    company_symbol = serializers.CharField(source='company.symbol', read_only=True)
    
    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'source', 'url', 'published_date', 'company_symbol']

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'