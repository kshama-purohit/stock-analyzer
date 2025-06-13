from django.shortcuts import render, redirect
from .models import Stock, Feedback
from plotly.offline import plot
import plotly.graph_objects as go
from .filters import StockFilter
import pandas as pd
from django.http import HttpResponseRedirect
from .utils import calculate_bollinger_bands, create_bollinger_chart, FeedbackForm
import plotly.express as px

def stockdata(request):
    stocks = Stock.objects.all()
    df = pd.DataFrame.from_records(stocks.values())

    fig = px.line(
        df,
        x = 'date',
        y = 'close',
        color = 'name',)
        # text = 'name',)
    fig.update_layout(
        title = "Closing Prices as a function of Time",
        xaxis_title = 'Date',
        yaxis_title = 'Closing Price',
        plot_bgcolor = 'beige'
        # text = 'name',
        # color = 'name',
    )
    # fig.update_traces(textposition='top center')
    stockdata = fig.to_html()
    context = {'stockdata': stockdata
               }
    return render(request, 'webapp/stockdata.html', context)
def index(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks
    }
    return render(request, 'webapp/index.html', context)


def candlestick_chart(request):

    queryset = Stock.objects.all().order_by('date')
    stock_filter = StockFilter(request.GET, queryset=queryset)
    filtered_qs = stock_filter.qs

    fig = go.Figure(data=[go.Candlestick(
        x=[obj.date for obj in filtered_qs],
        open=[obj.open for obj in filtered_qs],
        high=[obj.high for obj in filtered_qs],
        low=[obj.low for obj in filtered_qs],
        close=[obj.close for obj in filtered_qs]
    )])
    stock_names = filtered_qs.values_list('name', flat=True).distinct()
    stock_name = stock_names[0] if stock_names else "Selected Stock"
    fig.update_layout(
        title=f'Candlestick Chart for {stock_name}', 
        xaxis_title='Date', 
        yaxis_title='Closing Price',
        )
    
    fig.update_layout(hovermode="x")
    candlestick_chart = plot(fig, output_type='div')  # This gives HTML <div>

    return render(request, 'webapp/candlestick_chart.html', {
        'filter': stock_filter,
        'candlestick_chart': candlestick_chart
    })

def bollinger_bands(request):
    queryset = Stock.objects.all().order_by('date')
    stock_filter = StockFilter(request.GET, queryset=queryset)
    filtered_qs = stock_filter.qs
    stock_names = list(filtered_qs.values_list('name', flat=True).distinct())
    stock_name = stock_names[0] if stock_names else "Selected Stock"

    # Convert queryset to DataFrame for calculations
    data = {
        'Date': [obj.date for obj in filtered_qs],
        'Close': [obj.close for obj in filtered_qs]
    }
    
    df = pd.DataFrame(data)
    df.set_index('Date', inplace=True)

    # Calculate Bollinger Bands
    df = calculate_bollinger_bands(df)
    fig = create_bollinger_chart(df)
    stock_names = filtered_qs.values_list('name', flat=True).distinct()
    fig.update_layout(title=f'Bollinger Bands for {stock_name}', xaxis_title='Date', yaxis_title='Price')
    fig.update_layout(hovermode="x")
    bollinger_bands = plot(fig, output_type='div')
    return render(request, 'webapp/bollinger_bands.html', {
        'filter': stock_filter,
        'bollinger_bands': bollinger_bands
    })

def feedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST) #if they click the buttom -> post -> take the value and enter into form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ("/feedback/?submitted=True")
        
    else:
        form = FeedbackForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "webapp/feedback.html", {'form': form, 'submitted': submitted})

    

