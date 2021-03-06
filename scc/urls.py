"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

from . import views




urlpatterns = [
url(r'^$', views.index),
#url(r'^index', views.index),
url(r'^login/$',login, {'template_name': 'scc/login.html'}, name='login'),
url(r'^logout/$', logout,{'next_page': 'login'}, name='logout'),
url(r'^ingreso$', views.ingreso),
url(r'^enlace$', views.enlace),
url(r'^busqueda$', views.CorrespondenciaListView.as_view(),name="busqueda"),
url(r'^reportes$', views.reportes),
]
