from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', views.partner),
    url(r'^view_profile/$', views.view_profile),
    url(r'^edit_profile/$', views.edit_profile),
)
