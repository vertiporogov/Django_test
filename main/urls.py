from django.urls import path

from main.apps import MainConfig
from main.views import index, contact

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]