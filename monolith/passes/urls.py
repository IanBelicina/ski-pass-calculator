from django.urls import path
from .views import list_resorts

urlpatterns=[
    path("resorts/", list_resorts, name="list_resorts"),

]
