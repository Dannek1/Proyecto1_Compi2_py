from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.inicio, name='inicio'),
   # url(r'^Mesa', views.cerrar,name='Mesa'),
    url(r'^Mesa', views.mesa,name='Mesa'),
    url(r'^salir', views.inicio,name='salir'),
    #url(r'/(?P<nomb>\w{0,30}/(?)adfasdfdfdfdf/$',viewsfsdasd
]

