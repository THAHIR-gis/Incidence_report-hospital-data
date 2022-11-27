
from django.db import models
from django.contrib.gis.db import models #Geodjango Model Api

from django.contrib.gis.db import models as PointField
# Create your models here.
class incidence(models.Model):
  name = models.CharField(max_length=150)
  complaint=models.TextField(max_length=100)
  location = models.PointField(srid=4326,default='#1DB03C')
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name:'geometry'
    verbose_name_plural:'incidence'

class Export(models.Model):
    id_1 = models.CharField(max_length=66,blank=True,null=True)
    addr_state = models.CharField(max_length=6,blank=True,null=True)
    source = models.CharField(max_length=18,blank=True,null=True)
    website =  models.CharField(max_length=16,blank=True,null=True)
    amenity = models.CharField(max_length=8,blank=True,null=True)
    healthcare = models.CharField(max_length=8,blank=True,null=True)
    name = models.CharField(max_length=81,blank=True,null=True,default='no_name')
    ref = models.CharField(max_length=4,blank=True,null=True)
    fid = models.CharField(max_length=16,blank=True,null=True)
    addr_city = models.CharField(max_length=17,blank=True,null=True)
    addr_postc = models.CharField(max_length=6,blank=True,null=True)
    emergency = models.CharField(max_length=3,blank=True,null=True)
    addr_distr = models.CharField(max_length=10,blank=True,null=True)
    addr_full=models.CharField(max_length=42,blank=True,null=True)
    healthca_1 = models.CharField(max_length=31,blank=True,null=True)
    building = models.CharField(max_length=3,blank=True,null=True)
    survey_dat = models.CharField(max_length=10,blank=True,null=True)
    addr_house = models.CharField(max_length=28,blank=True,null=True)
    addr_stree = models.CharField(max_length=42,blank=True,null=True)
    note = models.CharField(max_length=85,blank=True,null=True)
    operator = models.CharField(max_length=43,blank=True,null=True)
    phone = models.CharField(max_length=16,blank=True,null=True)
    wheelchair = models.CharField(max_length=7,blank=True,null=True)
    email = models.CharField(max_length=32,blank=True,null=True)
    opening_ho = models.CharField(max_length=4 ,blank=True,null=True)
    name_en = models.CharField(max_length=55 ,blank=True,null=True)
    fax = models.CharField(max_length=7 ,blank=True,null=True)
    internet_a = models.CharField(max_length=4 ,blank=True,null=True)
    contact_ph = models.CharField(max_length=27 ,blank=True,null=True)
    operator_t = models.CharField(max_length=10 ,blank=True,null=True)
    descriptio = models.CharField(max_length=27 ,blank=True,null=True)
    office = models.CharField(max_length=23 ,blank=True,null=True)
    wikidata = models.CharField(max_length=9  ,blank=True,null=True)
    addr_place = models.CharField(max_length=9 ,blank=True,null=True)
    short_name = models.CharField(max_length=6 ,blank=True, null =True )
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
      return str(self.name)

class Hospital(models.Model):
  name = models.CharField(max_length=150)
  complaint=models.TextField(max_length=100)
  location = models.PointField(srid=4326)


  
  def __str__(self):
    return str(self.name)


