from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from iasip_api import views

urlpatterns = [
    url(r'^characters/$', views.CharacterList.as_view()),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.CharacterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
