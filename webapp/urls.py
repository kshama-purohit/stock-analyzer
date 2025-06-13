from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('candlestick_chart/', views.candlestick_chart, name='candlestick_chart'),
    path('bollinger_bands/', views.bollinger_bands, name='bollinger_bands'),
    path('stockdata/', views.stockdata, name = 'stockdata'),
    path('feedback/', views.feedback, name='feedback')
]