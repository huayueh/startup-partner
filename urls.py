from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer
import views

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', views.index),
    ('^admin/', include(admin.site.urls)),
    ('^signup/', views.signup),
    ('^partner/', views.partner),
    ('^business/', views.business),
)
