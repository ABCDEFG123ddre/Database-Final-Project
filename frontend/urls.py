from django.urls import path
from .views import *

app_name = "frontend"

urlpatterns = [
    path("", front, name = "front"),
    path("RAMPages/", RAMPages, name="RAMPages"),
    path("HDDPages/", HDDPages, name="HDDPages"),
    path("SSDPages/", SSDPages, name="SSDPages"),
    path("RAMdata/", RAMdata, name = "RAMdata"),
    path("HDDdata/", HDDdata, name = "HDDdata"),
    path("SSDdata/", SSDdata, name = "SSDdata"),
]