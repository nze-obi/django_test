from django.urls import path
from app.api import api
from app.views import home

urlpatterns = [
    path("", home),
    path("api/", api.urls),
]
