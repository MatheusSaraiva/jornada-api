from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from depoimentos.views import DepoimentosViewSet

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
