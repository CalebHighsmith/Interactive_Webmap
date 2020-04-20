import folium
import pandas

data = pandas.read_csv("Volanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
map = folium.Map(location=[80, -100], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon('green')))

map.add_child(fg)


map.save("Map1.html")