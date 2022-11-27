from  hotspot.models import incidence

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer #serializing into geoformat(lat/long)


class incidencelocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=incidence
        geo_field='location'
        fields='__all__'
class incidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=incidence
        fields='__all__'
