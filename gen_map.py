#gen_map.py. contains functions to generate map from 
# csv data, and are callable for data changes.

import gmplot as gp
import pandas as pd

#function using pandas to read information from csv into dataframe
#input: string name of csv to be read
#returns the dataframe to be used for map generation
def read_csv(name):
    df = pd.read_csv(filepath_or_buffer = name, header = 1, usecols = ["Latitude", "Longitude"])
    df = df.dropna()
    return df


#uses gmplot to plot map
#input: string name of the csv to pass to the read_csv funtion,
#string api key for google maps
# after drawing the map, it returns the name of the map html file
# to be added to the flask webpage
def generate_map(csv_name, api_key):
    df = read_csv(csv_name)
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
