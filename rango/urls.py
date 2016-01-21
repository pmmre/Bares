from django.conf.urls import patterns, url
from rango import views
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^bar/(?P<category_name_slug>[\w\-]+)/$', views.bar, name='bar'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_tapa/$', views.add_tapa, name='add_tapa'),
	url(r'^probando_ajax/$', views.probando_ajax, name='probando_ajax'),
	url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
	)
