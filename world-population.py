import folium

data=open('data/world.json', 'r', encoding='utf-8-sig').read()
map = folium.Map(location=[18.621994, 73.818411], zoom_start=4, tiles="Stamen Terrain")

fgpopulation = folium.FeatureGroup(name="Population")

fgpopulation.add_child(folium.GeoJson(data,
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                else 'orange' if x['properties']['POP2005'] <= 20000000
                                else 'red'}))

map.add_child(fgpopulation)
map.add_child(folium.LayerControl())

map.save("world-population.html")
