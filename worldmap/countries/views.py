from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Countrydata
from .serializers import CountryDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .functions import country_indentifier
from rest_framework.decorators import permission_classes
from rest_framework import permissions
class Country_data(APIView):

    @permission_classes([permissions.AllowAny,])
    def get(self, request, format=None):
        country_name = request.META['HTTP_NAME']
        country = Countrydata.objects.filter(name__startswith=country_name)
        serializer = CountryDataSerializer(country, many=True)
        return Response(serializer.data)

    @permission_classes([permissions.AllowAny,])
    def post(self,request,format = None):
        country_indentifier()
        return Response({'status':'sucessfully added'})

class Country_data_List(APIView):
    
    def get_object(self,id):
        try:
            return Countrydata.objects.get(id=id)
        except:
            pass 

    @permission_classes([permissions.AllowAny,])
    def get(self,request,id, format = None):
        country_name = request.META['HTTP_NAME']
        country = Countrydata.objects.filter(name__startswith=country_name)
        serializer = CountryDataSerializer(country, many=True)
        return Response(serializer.data)



    def put(self,request,id, format = None):
        country_name = self.get_object(id)
        serializer = CountryDataSerializer(country_name,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status':'data not correct'})
    
    def delete(self,request,id, format = None):
        country_name = self.get_object(id)
        country_name.delete()
        return Response({'status':'data deleted'})
