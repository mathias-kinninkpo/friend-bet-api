from django.conf.urls import include
from api import views
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register('groups', views.GroupViewset)

urlpatterns = [
    path(r'', include(router.urls))
]