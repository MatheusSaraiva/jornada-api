from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from depoimentos.views import Depoimentos_homeViewSet, DepoimentosViewSet

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet)
router.register('depoimentos-home', Depoimentos_homeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
