from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^urls/$', views.view_all, name='all_urls'),
    url(r'^add/url/$', views.view_add_url, name='add_url'),
]