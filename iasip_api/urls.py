from django.conf.urls import url
from iasip_api import views
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
schema_view = get_schema_view(title="It's Always Sunny in Philadelphia API")

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^characters/$', views.CharacterList.as_view()),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.CharacterDetail.as_view()),
    url(r'^schemas/$', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)