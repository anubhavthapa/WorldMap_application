import pycountry
import os
import json
from geopy.geocoders import Nominatim
from .models import Countrydata
from .serializers import CountryDataSerializer

def geo_identifier(name):
    geo_data=None
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_dir=os.path.join(BASE_DIR,(r'countries\data\allcountry.json'))
    # print(new_dir)
    with open(new_dir,'r') as json_file:
        new_json=json.load(json_file)
        filt_json=new_json['features']
        for country in range(len(filt_json)):
            if filt_json[country]["properties"]['A3'] == name:
                geo_data= filt_json[country]
    return geo_data 

def lat_long_getter(string):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(string)
    new_lat=location.latitude
    new_lon=location.longitude
    obj={'latitude':new_lat,'longitude':new_lon}
    return obj


def geo_converter(name):
    country_name=pycountry.countries.search_fuzzy(name)
    alpha=country_name[0].alpha_3
    geo_converted=geo_identifier(alpha)
    lat_long_data=lat_long_getter(name)
    geo_converted.update(lat_long_data)
    geo_data = geo_converted
    updated_data = {'name':name,'geojson':geo_data}
    serializer = CountryDataSerializer(data = updated_data)
    
    if serializer.is_valid():
            serializer.save()
    else:
        print(serializer.errors)
         
    return updated_data
    

def country_indentifier():
    geo_data=None
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_dir=os.path.join(BASE_DIR,(r'countries\data\country.json'))
    with open(new_dir,'r') as json_file:
        new_json=json.load(json_file)
        
        for i in range(len(new_json)):
            try:
                geo_converter(new_json[i]['name'])
            except:
                pass

