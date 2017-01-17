from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_all, name='all_urls'),
    url(r'^add/url/$', views.view_add_url, name='add_url'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='redirection_url'),
]