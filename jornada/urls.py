from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from depoimentos.views import Depoimentos_homeViewSet, DepoimentosViewSet
from destino.views import DestinosViewSet

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename="Depoimentos")
router.register('depoimentos-home', Depoimentos_homeViewSet, basename="Depoimentos_home")
router.register('destinos', DestinosViewSet, basename="Destinos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
