from django.urls import path
from . import views



urlpatterns = [
    path("", views.index , name="index"),
    path("<int:num1>/" , views.mert , name="yol"),
    path("<str:item>/",views.courses,name="course"),
    path("<int:num1>/<int:num2>/" , views.carpma , name="multiply"),
]
