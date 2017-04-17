from django.conf.urls import url
from iasip_api import views

urlpatterns = [
    url(r'^characters/$', views.character_list),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.character_detail),
]
