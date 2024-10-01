from django.db import models
from django_countries.fields import CountryField
from taggit.managers import TaggableManager

class Organisation(models.Model):

    name = models.CharField(max_length=64)
    country = CountryField()

    @property
    def organisation_attributes(self):
        return self.attributes.objects.all()

# Kenya - County, Sub-County
# Uganda - Region, Sub-Region, District, County
class Attribute(models.Model):

    name = models.CharField(max_length=64)
    choices = models.JSONField()
    tags = TaggableManager()
    

class OrganisationAttribute(models.Model):

    organisation = models.ForeignKey(Organisation,on_delete=models.PROTECT, related_name="attributes")
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name="+")
    value = models.CharField(max_length=64)