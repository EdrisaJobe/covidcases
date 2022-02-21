from django.shortcuts import render
import plotly.express as px
import pandas as pd
import requests

# Create your views here.
def index(request):
    
    # setting up variables
    data = True
    res = None
    summary = None
    
    # checking to make sure data is retrievable
    while data:
        try:
            res = requests.get('https://api.covid19api.com/summary')
            data = False
            summary = res.json()['Global']
        except:
            data = True
    return render(request, 'index.html',{'summary':summary})