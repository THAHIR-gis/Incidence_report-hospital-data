
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from . models import *
from .models import Export
# Register your models here.

# @admin.register(incidence)
# class incidenceAdmin(LeafletGeoAdmin):
#   list_display=('name','complaint','location','created_at','updated_at')
# admin.site.register(incidence)

# @admin.register(incidence)
# class incidenceAdmin(admin.LeafletGeoAdmin):
#     list_display=('name','complaint','location','created_at','updated_at')


@admin.register(incidence)
class incidenceAdmin(LeafletGeoAdmin):
    list_display = ( "name", "complaint", "location")


@admin.register(Export)   
class exportAdmin(LeafletGeoAdmin):
    # List_display =('amenity',' area','healthcare','fid','emergency','source','website','building',' operator','ref','opening_ho','fax ','healthca_1 ','address','operational ','level ','geom')    
    List_display=('__all__')



    