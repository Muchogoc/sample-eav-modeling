from .views import OrganisationViewset, AttributeViewset, OrganisationAttributeViewset

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'organisations', OrganisationViewset)
router.register(r'attributes', AttributeViewset)
router.register(r'organisation-attributes', OrganisationAttributeViewset)