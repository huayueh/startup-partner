from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', views.partner),
    url(r'^view_profile/$', views.view_profile),
    url(r'^edit_profile/$', views.edit_profile),
    url(r'^user_detail/$', views.user_detail),
    url(r'^view_category/$', views.view_category),
    url(r'^search/$', views.partner_search),
)
