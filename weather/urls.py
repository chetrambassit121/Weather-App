"""the_weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(),name='home'),
    path('upload', views.simple_upload, name="upload"),
    path('delete/<city_name>/',views.delete_city, name='delete_city'),
    path('weather_search', views.SearchWeather.as_view(), name="weather_search"),
    path('google_sheets', views.google_sheets, name="google_sheets"),
]
