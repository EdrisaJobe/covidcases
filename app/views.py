from django.shortcuts import render
import pandas as pd
import requests
import folium

# Create your views here.
def index(request):
    
    # setting up variables
    data = True
    res = None
    summary = None
    
    # checking to make sure data is retrievable
    while data:
        try:
            res = requests.get('https://thevirustracker.com/free-api?global=stats')
            summary = res.json()['Global']
            data = False
        except:
            data = True
    return render(request, 'index.html',{'summary':summary})

def map(request):
    
    # getting the csv of the countries
    cases = pd.read_csv('countries.csv')
    
    # api request -> to json
    req = requests.get("https://thevirustracker.com/free-api?global=stats")
    global_cases = req.json()
    print(global_cases)
    
    # data frame for map
    df = []
    for j in range(1,len(global_cases['countryitems'][0])):
        df.append([global_cases['countryitems'][0][f'{j}']['title'],
                   global_cases['countryitems'][0][f'{j}']['total_cases']])
    
    # setting variables for the data frame
    df_covid = pd.DataFrame(df,columns=['Country','Total Case'])
    
    # giving the countries a new name
    df_covid.replace('USA', "United States of America", inplace = True)
    df_covid.replace('Tanzania', "United Republic of Tanzania", inplace = True)
    df_covid.replace('Democratic Republic of Congo', "Democratic Republic of the Congo", inplace = True)
    df_covid.replace('Congo', "Republic of the Congo", inplace = True)
    df_covid.replace('Lao', "Laos", inplace = True)
    df_covid.replace('Syrian Arab Republic', "Syria", inplace = True)
    df_covid.replace('Serbia', "Republic of Serbia", inplace = True)
    df_covid.replace('Czechia', "Czech Republic", inplace = True)
    df_covid.replace('UAE', "United Arab Emirates", inplace = True)
    
    # countries collection
    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    country_cases = f'{url}/world-countries.json'
    
    m = folium.Map(zoom_start=2)
    
    # adding Choropleth layer for the map using the above url
    folium.Choropleth(
        geo_data=country_cases,
        name='choropleth',
        data=df._covid,
        colums=['Country','Total Case'],
        key_on='feature.properties.name',
        fill_color='PuRd',
        nan_fill_color='white' 
    ).add_to(m)
    folium.LayerControl().add_to(m)
    
    # looping through the data and appending it to map 'm'
    for lat,lon,name, in zip(cases['latitude'],cases['longitude'],cases['name']):
        folium.Circle(
            redius=100,
            location=[lat,lon],
            popup=name,
            fill=True,
            fill_color='red',
        ).add_to(m)
        
    m = m._repr_html_()
    
    data = True
    res = None
    
    # getting country information
    countries = None
    
    # while data == True, collect info based on countries from API
    while data:
        try:
            res = requests.get('https://api.covid19api.com/summary')
            json = res.json()
            countries = json['Countries']
            data=False
        except:
            data=True
    
    return render(request,'map.html', {'countries':countries, 'm':m})