def gen_map():
  sound_map = pan.read_csv("UCSC_Sound_Map.csv",skiprows=1,usecols = ["Latitude","Longitude"])
  sound_map = sound_map.dropna(0,'any')
  longs = sound_map["Longitude"]
  lats = sound_map["Latitude"]

  #creating map
  new_map = gmp.GoogleMapPlotter(36.99,-122.0582,15)

  new_map.scatter(lats, longs, '#3B0B39', size=40, marker=False)
  link = "my_other_map.html"
  new_map.draw(link)
