from .models import Organisation, Attribute, OrganisationAttribute
from django_filters import rest_framework as filters


class OrganisationAttributeFilter(filters.FilterSet):

   class Meta:
        model = OrganisationAttribute
        fields = "__all__"

class OrganisationFilter(filters.FilterSet):

    class Meta:
        model = Organisation
        fields = "__all__"

class AttributeFilter(filters.FilterSet):

    class Meta:
        model = Attribute
        fields = ["name"]