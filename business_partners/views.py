from rest_framework import viewsets
from .models import Organisation, Attribute, OrganisationAttribute
from .serializers import OrganisationSerializer, AttributeSerializer, OrganisationAttributeSerializer
from .filters import OrganisationFilter, AttributeFilter, OrganisationAttributeFilter



class OrganisationViewset(viewsets.ModelViewSet):
    
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    filterset_class = OrganisationFilter

class AttributeViewset(viewsets.ModelViewSet):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    filterset_class = AttributeFilter

class OrganisationAttributeViewset(viewsets.ModelViewSet):

    queryset = OrganisationAttribute.objects.all()
    serializer_class = OrganisationAttributeSerializer
    filterset_class = OrganisationAttributeFilter