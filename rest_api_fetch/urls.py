from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('model/',views.Model_list),
    path('model/<int:id>/',views.Modeldetail)


]
