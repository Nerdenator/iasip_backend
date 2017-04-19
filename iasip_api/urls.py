from django.conf.urls import url, include
from iasip_api import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="It's Always Sunny in Philadelphia API")



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^characters/$', views.CharacterList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^schemas/$', schema_view),
]
