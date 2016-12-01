"""Catch_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from online_list import urls as online_urls
#from knowledge import urls as knowledge_urls
from online_list import views
import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    #url(r'^analysis/', views.analysis_index, name="analysis"),
    url(r'^online_list/', include(online_urls)),

    #url("^assets/$", views.assets_index, name="assets"),
    #url("^monitor/$", views.monitor_index, name="monitor"),
    #url(r'^knowledge/', include(knowledge_urls)),
    #url("^login/$", views.acc_login, name="login"),
    #url("^logout/$", views.acc_logout, name="logout")

]
