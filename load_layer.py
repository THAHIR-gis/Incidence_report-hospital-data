import os
from django.contrib.gis.utils import LayerMapping
from .models import Export
from django.contrib.gis.db import models
from hotspot import load_layer
from django.contrib.gis.gdal.error import GDALException
export_mapping = {
    'id_1': 'id_1',
    'amenity': 'amenity',
    'healthcare': 'healthcare',
    'name': 'name',
    'ref': 'ref',
    'fid': 'FID',
    'addr_city': 'addr_city',
    'addr_postc': 'addr_postc',
    'emergency': 'emergency',
    'addr_distr': 'addr_distr',
    'addr_full': 'addr_full',
    'addr_state': 'addr_state',
    'source': 'source',
    'website': 'website',
    'healthca_1': 'healthca_1',
    'building': 'building',
    'survey_dat': 'survey_dat',
    'addr_house': 'addr_house',
    'addr_stree': 'addr_stree',
    'note': 'note',
    'operator': 'operator',
    'phone': 'phone',
    'wheelchair': 'wheelchair',
    'email': 'email',
    'opening_ho': 'opening_ho',
    'name_en': 'name_en',
    'fax': 'fax',
    'internet_a': 'internet_a',
    'contact_ph': 'contact_ph',
    'operator_t': 'operator_t',
    'descriptio': 'descriptio',
    'office': 'office',
    'wikidata': 'wikidata',
    'addr_place': 'addr_place',
    'short_name': 'short_name',
    'geom': 'MULTIPOINT',
}

export_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'calicut_shapefile/export1.shp'))

def run(verbose=True):
    lm=LayerMapping(Export,export_shp,export_mapping,transform=False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)