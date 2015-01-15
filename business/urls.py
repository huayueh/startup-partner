from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', views.business),
    url(r'^add_business/$', views.add_business),
    url(r'^insert_business/$', views.insert_business),
)
