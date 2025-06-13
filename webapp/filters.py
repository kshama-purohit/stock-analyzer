import django_filters
from .models import Stock
from django import forms

def get_unique_choices():
    unique_values =Stock.objects.values_list('name', flat=True).distinct()
    choices = [(value, value) for value in unique_values]
    return choices

class StockFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte', label = 'From Date', widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}))
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte', label = 'To Date', widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}))
    name = django_filters.ChoiceFilter(field_name="name", lookup_expr='icontains', label = 'Stock Name', choices=get_unique_choices)

    class Meta:
        model = Stock
        fields = ['start_date', 'end_date', 'name']
        order_by = ['-date']


    