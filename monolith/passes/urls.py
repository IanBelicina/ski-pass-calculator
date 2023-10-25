from django.urls import path
from .views import list_resorts, show_resort

urlpatterns=[
    path("resorts/", list_resorts, name="list_resorts"),
    path("resorts/<int:id>", show_resort, name="show_resort"),

]
