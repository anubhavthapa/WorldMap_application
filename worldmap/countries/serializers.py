from .models import Countrydata
from rest_framework import serializers
import pycountry
class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countrydata
        fields = ['id','name','geojson','added_date']