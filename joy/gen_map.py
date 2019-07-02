#gen_map.py. contains functions to generate map from 
# csv data, and are callable for data changes.

import requests
import os
import io
import pandas as pd
import gmplot as gp

#function using pandas to read information from csv into dataframe
#input: none, use saved link of spreadsheets
#returns the dataframe to be used for map generation
def read_csv():
    r = requests.get('https://docs.google.com/spreadsheets/d/1_4v6PQ3asgZ-5I5bI8jObU2bmccdgmW_gA-m_99hzss/export?format=csv&id=1_4v6PQ3asgZ-5I5bI8jObU2bmccdgmW_gA-m_99hzss')
    data = r.text
    buffer = io.StringIO(data)
    df = pd.read_csv(filepath_or_buffer = buffer , header = 1, usecols = ["Latitude", "Longitude"])
    df = df.dropna()
    return df


#uses gmplot to plot map
#input: string api key for google maps
# after drawing the map, it returns the name of the map html file
# to be added to the flask webpage
def generate_map(api_key):
    df = read_csv()
    map1 = gp.GoogleMapPlotter(36.993600, -122.059900, 14) 
    map1.apikey = api_key
    lon = tuple(df.Longitude)
    lat = tuple(df.Latitude)
    map1.scatter(lat, lon,'red', size=40, marker=False)
    for i in range(len(lat)):
        map1.marker(lat[i], lon[i], 'red')
    html_loc = "templates/joy_map.html"
    map1.draw(html_loc)
    return html_loc

