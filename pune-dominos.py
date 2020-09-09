import folium
import pandas

data = pandas.read_csv("data/dominos.txt")
print(data)

lat = list(data["LAT"])
lon = list(data["LON"])
address = list(data["Address"])
locality = list(data["Locality"])


def color_producer(locality):
    if locality == 'Pimpri':
        return 'green'
    elif locality == 'Pune':
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[18.621994, 73.818411], zoom_start=10, tiles="Stamen Terrain")
fgdominos = folium.FeatureGroup(name="Domino's")

for lt, ln, addr, loc in zip(lat, lon, address, locality):
    fgdominos.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=str(addr),
    fill_color=color_producer(loc), fill=True,  color='grey', fill_opacity=0.7))



fgpopulation = folium.FeatureGroup(name="Population")

fgpopulation.add_child(folium.GeoJson(data=open('data/world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgdominos)
map.add_child(fgpopulation)
map.add_child(folium.LayerControl())

map.save("pune-dominos.html")
