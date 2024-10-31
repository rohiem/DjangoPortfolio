from django.conf import settings
from django.urls import path, include
from .views import models,modeldetail


app_name = 'portfolio'
urlpatterns = [

    path('models',models , name="models"),
    path('models/<slug:slug>',modeldetail , name="modeldetail"),
]