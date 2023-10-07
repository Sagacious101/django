from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    path('greet/<str:name>', greet),
    path('itisnewyear', it_is_new_year)
]