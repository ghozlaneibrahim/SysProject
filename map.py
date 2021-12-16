import folium
from folium.map import Tooltip
from geopy.geocoders import Nominatim
import os


## fog hadi ndiro win lazm user ymed les images w  7na njbdo les cites
## hna yjbed city w cooridnation ta3hom w ykhdmlhom markers
geolocator = Nominatim(user_agent="CityFinder")
location = geolocator.geocode("alger")

style2 = {'fillColor': '#228B22', 'color': '#eedcdd'}
# create map object
print(location)
print(location.latitude, location.longitude)


m = folium.Map(
    location=[location.latitude, location.longitude],
    tiles="http://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg'",
    zoom_size=2.5,
    attr="My Data Attribution",
)


overlay = os.path.join('maroc.geojson')

folium.GeoJson(overlay, style_function=lambda x:style2).add_to(m)

folium.Marker(
    [location.latitude, location.longitude],
    popup="<strong> location </strong>",
    icon=folium.Icon(color="red"),
).add_to(m)


# w hna t7t ydir surface w yrsom tmnkii7 hadak w nchlh nkono kmlna

# Genereate map
m.save("map.html")
