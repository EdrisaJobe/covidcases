from django.shortcuts import render

# math formation/visualization
import pandas as pd
import requests
import folium
import json

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
            summary = res.json()['Global']
            data = False
        except:
            data = True
    return render(request, 'index.html',{'summary':summary})

def map(request):
    
    # reading the csv file and stting a display
    data = pd.read_csv('countries.csv')
    pd.set_option('display.max_rows',3)
    
    # folium map bootup information
    m = folium.Map(location=[0,0], tiles='cartodbpositron', zoom_start=3)
    
    # looping through the csv and displaying each individual data based on indexing
    for i in range(0, len(data)):
        
        # getting country coords
        lat = float(data.iloc[i]['Latitude'])
        lon = float(data.iloc[i]['Longitude'])
        
        # grabbing the lat and lon for all country location and setting a circle marker
        folium.CircleMarker([lat,lon], popup=int(data.iloc[i]['Deaths']), radius=5, color='red', fill=True).add_to(m)
        
    m = m._repr_html_()
    
    data = True
    res = None
    
    # getting country information
    countries = None
    
    # while data == True, collect info based on countries from API
    while data:
        try:
            res = requests.get('https://api.covid19api.com/summary')
            json_data = res.json()
            countries = json_data['Countries']
            data=False
        except:
            data=True
    
    return render(request,'map.html', {'countries':countries, 'm':m})