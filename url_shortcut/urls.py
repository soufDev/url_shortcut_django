from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_all, name='all_urls'),
    url(r'^add/url/$', views.URLCreate.as_view(), name='add_url'),
    url(r'^edit/(?P<code>\w{6})$', views.URLUpdate.as_view(), name='update_url'),
    url(r'^delete/(?P<code>\w{6})$', views.URLDelete.as_view(), name='delete_url'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='redirection_url'),
]