from django.contrib import admin
from django.urls import path, include
from business_partners.urls import router as bp_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bps/', include(bp_router.urls)),
]
