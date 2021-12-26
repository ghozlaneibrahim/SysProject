import folium
from folium.map import Tooltip
from geopy.geocoders import Nominatim
import os
import json


## fog hadi ndiro win lazm user ymed les images w  7na njbdo les cites
style2 = {"fillColor": "#228B22", "color": "#eedcdd"}
locations = []
## hado les cites li ra7 n7wso 3lihom ki shkopi mohim dert tableau ana bash ntesto brk

for city in ["Mekka", "alger", "Berlin"]:
    geolocator = Nominatim(user_agent="CityFinder")
    ## hna yjbed city w cooridnation ta3hom
    locations.append(geolocator.geocode(city))


# create map object

location = locations[0]
print(locations[2])

# hna yakhdm map
m = folium.Map(
    location=[location.latitude, location.longitude],
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    zoom_size=40,
    zoom_start = 3,
    attr="My Data Attribution",
)
<<<<<<< HEAD

f = open("Shape.json")
=======
# makacho had el fichier 3endi ana 
#print("okk")
f = open("maroc.json")
>>>>>>> 0990c684c91af11110191e29266f09ef961eb4c3


data = json.loads(f.read())
citiesCord = data["features"][0]["geometry"]["coordinates"][0]
for i in range(0, len(locations)):
    data["features"][0]["geometry"]["coordinates"][0].append(
        [locations[i].longitude, locations[i].latitude]
    )

for cityCord in citiesCord:

    folium.GeoJson(data, style_function=lambda x: style2).add_to(m)

    folium.Marker(
        [cityCord[1], cityCord[0]],
        popup="<strong> location </strong>",
        icon=folium.Icon(color="red"),
    ).add_to(m)


# w hna t7t ydir surface w yrsom tmnkii7 hadak w nchlh nkono kmlna

# Genereate map
m.save("map.html")
