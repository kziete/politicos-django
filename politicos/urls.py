"""politicos URL Configuration

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
from django.contrib import admin
import settings

from sitio import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    
    url(r'^$', views.Home.as_view(), name='home'),

    url(r'^login', views.LoginView.as_view(),name="login"),
    url(r'^logout', views.logout, name="logout"),    
    url(r'^registro', views.RegistroView.as_view(),name="registro"),

    url(r'^(?P<slug>[-\w]+)$',views.DetallePolitico.as_view(),name="detalle-politico"),
    url(r'^(?P<politico>[-\w]+)/denuncia$',views.DenunciaEvento.as_view(),name="denuncia-evento"),
    url(r'^(?P<politico>[-\w]+)/(?P<slug>[-\w]+)$',views.DetalleEvento.as_view(),name="detalle-evento"),

    
]
