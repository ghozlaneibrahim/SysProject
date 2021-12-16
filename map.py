import folium
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="CityFinder")
location = geolocator.geocode("laghouat")
#create map object
print(location.latitude, location.longitude)
m = folium.Map(location=[location.latitude, location.longitude],zoom_size=30)

# Genereate map 
m.save('map.html')