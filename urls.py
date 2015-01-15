from django.conf.urls import patterns, url, include
from django.contrib import admin
import dbindexer
import views

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    url(r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^add_user/$', views.add_user),
    url(r'^check_user_exist/$', views.check_user_exist),
    url(r'^partner/$', include('partner.urls')),
    url(r'^business/', include('business.urls')),
    url(r'^tinymce/$', views.tinymce),
)
