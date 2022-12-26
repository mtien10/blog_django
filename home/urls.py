from django.urls import path
from home.views import *

urlpatterns = [
    path('', index),
    path('info/', info),
    path('contact/', contact)
]