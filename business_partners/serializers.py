from rest_framework import serializers
from .models import Organisation, Attribute, OrganisationAttribute
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class AttributeSerializer(TaggitSerializer,serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Attribute
        fields = "__all__"

class OrganisationAttributeSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = OrganisationAttribute
        fields = "__all__"

class OrganisationSerializer(serializers.ModelSerializer):

    attributes = OrganisationAttributeSerializer(source="organisation_attributes",read_only=True)

    class Meta:
        model = Organisation
        fields = "__all__" 



