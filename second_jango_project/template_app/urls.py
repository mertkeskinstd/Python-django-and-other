from django.urls import path
from . import views
app_name="template_app"
urlpatterns= [
    path("template/",views.index,name="index"),
    path("weather/",views.weather,name="weather")
    
]