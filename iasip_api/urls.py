from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from iasip_api import views

urlpatterns = [
    url(r'^characters/$', views.character_list),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.character_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
