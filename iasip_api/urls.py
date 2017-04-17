from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from iasip_api import views


# API endpoints

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^characters/$',
        views.CharacterList.as_view(),
        name='character-list'),
    url(r'^characters/(?P<pk>[0-9]+)/$',
        views.CharacterDetail.as_view(),
        name='character-detail'),
    url(r'^characters/(?P<pk>[0-9]+)/highlight/$',
        views.CharacterHighlight.as_view(),
        name='characters-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])



urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
]

