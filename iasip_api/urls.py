from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from iasip_api import views

urlpatterns = [
    url(r'^characters/$', views.CharacterList.as_view()),
    url(r'^characters/(?P<pk>[0-9]+)/$',views.CharacterDetail.as_view()),
    url(r'^crimes/$', views.CrimeList.as_view()),
    url(r'^crimes/(?P<pk>[0-9]+)/$', views.CrimeDetail.as_view()),
    url(r'^character_crimes/$', views.CharacterCrimeList.as_view()),
    url(r'^character_crimes/(?P<pk>[0-9]+)/$', views.CharacterCrimeDetail.as_view()),
    url(r'^character_crimes/(?P<name>)/$', views.CharacterCrimeListByCharacter.as_view())
]