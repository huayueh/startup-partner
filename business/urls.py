from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', views.business),
    url(r'^add_business/$', views.add_business),
    url(r'^insert_business/$', views.insert_business),
    url(r'^biz_detail/$', views.business_detail),
    url(r'^view_category/$', views.view_category),
    url(r'^search/$', views.business_search),
)
