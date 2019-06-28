import gmplot as gp
import pandas as pd

def read_csv(name):
    df = pd.read_csv(filepath_or_buffer = name, header = 1, usecols = ["Latitude", "Longitude"])
    df = df.dropna()
    return df

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
