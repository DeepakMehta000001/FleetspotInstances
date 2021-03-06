"""fleetSpotInstance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboard.views import signup,home,loginUser,dashboard_config,fleet_request


urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^login/$',loginUser,name='login'),
    url(r'^dashboard/$',dashboard_config,name='config'),
    url(r'^request/$',fleet_request,name='fleet_request'),
    url(r'^register/$',signup,name='register'),
    url(r'^admin/', admin.site.urls),
]
