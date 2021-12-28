import folium
from folium.map import Tooltip
import os
import json
import func



## fog hadi ndiro win lazm user ymed les images w  7na njbdo les cites
style2 = {"fillColor": "#228B22", "color": "#eedcdd"}
# create map object
locations = [func.image_coordinates('photo{}.jpg'.format(i)) for i in range(2,5)]






location = locations[0]
# hna yakhdm map
m = folium.Map(
    location=[location.latitude, location.longitude],
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    zoom_size=20,
    zoom_start = 10,
    attr="My Data Attribution",
)


f = open("Shape.json")



data = json.loads(f.read())
citiesCord = data["features"][0]["geometry"]["coordinates"][0]
for i in range(0, len(locations)):
    if locations[i] != "" :
        data["features"][0]["geometry"]["coordinates"][0].append(
            [locations[i].longitude, locations[i].latitude]
        )
i =1
for cityCord in citiesCord:

    folium.GeoJson(data, style_function=lambda x: style2).add_to(m)

    folium.Marker(
        [cityCord[1], cityCord[0]],
        popup="<strong> photo{} </strong>".format(i),
        icon=folium.Icon(color="red"),
    ).add_to(m)
    i+=1


# w hna t7t ydir surface w yrsom tmnkii7 hadak w nchlh nkono kmlna

# Genereate map
m.save("map.html")
