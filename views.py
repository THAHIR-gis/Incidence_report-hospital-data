
from django.shortcuts import render,HttpResponse

from django.views.generic import TemplateView
from django.db import migrations

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import incidence,Export
from django.http import HttpResponse
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# REST_FRAMEWORK-GIS
from rest_framework import generics
from django.contrib.gis.geos import point
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import GEOSGeometry
from  .models import Export
#SERIALIZER
from .serializer import *
from django.views.decorators.csrf import csrf_exempt   
from hotspot.views import incidenceSerializer
from django.http import JsonResponse
from django.core.serializers import serialize


from sys import argv
from os.path import exists

import json

# Create your views here.

# geolocator=Nominatim(user_agent='location')

# class ListCreateGenericViews(generics.ListCreateAPIView):
#     queryset=incidence.objects.all()
#     serializer_class=incidenceSerializer

# def perform_create(self,serilizer):
#      name=serializer.initial_data['name']
#      g=geolocator.geocode(name) 
#      lat=g.latitude
#      lng=g.longitude
#      pnt=point(lat,lng) 
#      print(pnt)
#      serializer.save(location=pnt)  


# class incidenceUpdateRetriveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=incidence.objects.all()
#     serializer_class=incidenceSerializer

# def perform_update(self,serializer):
#      name=serializer.initial_data['name']
#      g=geolocator.geocode(name)
#      lat=g.latitude
#      lng=g.longitude
#      pnt=point(lat,lng)
#      print(pnt)
#      serializer.save(location=pnt)    


@csrf_exempt
def centersapi(request):
    if request.method=='GET':
        snippets=incidence.objects.all()   #get all the models field 
        s=incidenceSerializer(snippets,many=True) #serialize them
        return JsonResponse(s.data,safe=False)  #return json

    elif request.method=='POST': #checking method
        dataset=JSONparse().parse(request) #stored requested parsed data into a variable 
        serializer=serializers.incidenceSerializer(data=dataset) #converting through serializing json format to complex datatype(ORM)
        if serializer .is_valid(): #comforming if the data type is complex datatype
            serializer.save() #if yes save the complex data
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)      

    

# def upload_node(request):
#     template = "geojson.html"
#     form = incidenceSerializer()
#     if request.method == 'GET':
#         form = incidenceSerializer(request.POST)
#         if serializer.is_valid():
#             network_fk = form.cleaned_data['nework']



def index(request):

    return render(request,'index.html')
def leaflet(request):
    a=incidence.objects.all()
    return render(request,'leaflet.html',{'x':a})
    
def Export_dataset(request):
    export=serialize('geojson',Export.objects.all())
    return HttpResponse(export,content_type='json')    

class HomeView(TemplateView):

      pass
class incidenceAPI(generics.ListAPIView):
    queryset=incidence.objects.all()
    serializer_class=incidenceSerializer
     
def incidences(self):
    incidences=incidence.objects.all()
    return serializer.serialize('json',incidences)     

def drone(request):
    return render(request,'update.html')

# name=vinayk
# compalint=bad hospital
# h_name=kims
# a=Hospital.objects.filter(hospital_name=name)



# geojson = {
#     "type": "FeatureCollection",
#     "features": [
#     {
#         "type": "Feature",
#         "geometry" : {
#             "type": "Point",
#             "coordinates": [d["lon"], d["lat"]],
#             },
            
#         "properties" : d,
        

#      } for d in data]
     
# }


# output = open(out_file, 'w')
# json.dump(geojson, output)

# print (geojson)


# outGeoJson = {}
# outGeoJson['properties'] = inJson
# outGeoJson['type']= "Feature"
# outGeoJson['geometry']= {"type": "Point", "coordinates":
#     [inJson['loc_lng'], inJson['loc_lng']]}

# console.log(outGeoJson)

# # longitude = 11.2404
# latitude = 75.8156

# user_location = Point(longitude, latitude, srid=4326)

# class Home(generic.ListView):
#     model = incidence
#     context_object_name = 'hotspot'
#     queryset = incidence.objects.annotate(distance=Distance('location',
#     user_location)
#     ).order_by('distance')[0:6]
#     template_name = 'index.html'



# def function_ff(request):
#     # if request=='POST':
#     if request.method == 'POST':
#             datafile = request.FILES['data_file']
#             objects = json.load(datafile)
#             for object in objects['features']:
#                 properties = object['properties']
#                 geometry = object['geometry']
                
#                 name = properties.get('name', 'no-name')
#                 location = fromstr(geometry.get('geometry'),srid=4326)
#                 incidence(name=name, location = location).save()
                # a=incidence.objects.create('name','complaint','location')
                



              


    # #   return HttpResponse('bingo')
    # return render(request,'update.html')





# def UpdateWmsView(request):
#  drone = L.tileLayer.wms("http://localhost:8080/geoserver/kozhikode/wms", {
#   layers: '	kozhikode:export_NEW2',
#   format: 'image/png',
#   transparent: true,
#   attribution: "mylayer"
# });
# drone.addTo(map) 
