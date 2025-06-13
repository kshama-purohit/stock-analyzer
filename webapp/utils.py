import pandas as pd
from django import forms
import plotly.graph_objects as go
from django.forms import ModelForm
from .models import Feedback

def calculate_bollinger_bands(data, window=20, num_std=2):
         df = pd.DataFrame(data)
         df['SMA'] = df['Close'].rolling(window).mean()
         df['StdDev'] = df['Close'].rolling(window).std(ddof=0)
         df['Upper'] = df['SMA'] + num_std * df['StdDev']
         df['Lower'] = df['SMA'] - num_std * df['StdDev']
         return df

def create_bollinger_chart(df):
         fig = go.Figure()
         fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Close Price'))
         fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], name='SMA'))
         fig.add_trace(go.Scatter(x=df.index, y=df['Upper'], name='Upper Band'))
         fig.add_trace(go.Scatter(x=df.index, y=df['Lower'], name='Lower Band', fill='tonexty'))
         fig.update_layout(title='Bollinger Bands', xaxis_title='Date', yaxis_title='Price')
         return fig

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        labels = {
               'name': '',
               'email':'',
               'feedback':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter First & Last Name', 'class':'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email ID','class':'form-input'}),
            'feedback': forms.Textarea(attrs={'placeholder': 'Enter Feedback','class':'form-input'})
        }


