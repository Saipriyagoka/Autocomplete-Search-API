"""Mve_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', views.MovieList.as_view(), name='movielist'),
    url(r'^SuggestProject/', views.ajax_load_project, name='ajax_load_project'),
    url(r'^$', views.searchProject, name='searchProject'),
]
