from django.conf.urls.defaults import patterns, include, url
from webadmin.core import views, models
from django.contrib import auth

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webadmin.views.home', name='home'),
    # url(r'^webadmin/', include('webadmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'webadmin.core.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^current_proj/$', views.modellist, {'model' : models.Proj}),
    url(r'^history_proj/$', views.modellist, {'model' : models.Task}),
    url(r'^host/$', views.modellist, {'model' : models.Host}),
    url(r'^idc/$', views.modellist, {'model' : models.IDC}),
    url(r'^ip/$', views.modellist, {'model' : models.IP}),
    url(r'^user/$', views.modellist, {'model' : auth.models.User}),
    url(r'^exec_proj/$', views.exec_proj),
    url(r'current_proj/add/$', views.add_proj),
    url(r'current_proj/(?P<id>[^/]+)/$', views.edit_proj),               
    url(r'current_proj/delete/(?P<id>[^/]+)/$', views.del_proj),
    url(r'history_proj/view/(?P<id>[^/]+)/$', views.view_log),
    url(r'host/add/$', views.add_host),
    url(r'host/(?P<id>[^/]+)/$', views.edit_host),               
    url(r'host/delete/(?P<id>[^/]+)/$', views.del_host),
    url(r'idc/add/$', views.add_idc),
    url(r'idc/(?P<id>[^/]+)/$', views.edit_idc),               
    url(r'idc/delete/(?P<id>[^/]+)/$', views.del_idc),
    url(r'ip/add/$', views.add_ip),
    url(r'ip/(?P<id>[^/]+)/$', views.edit_ip),               
    url(r'ip/delete/(?P<id>[^/]+)/$', views.del_ip),
    url(r'user/add/$', views.add_user),
    url(r'user/(?P<id>[^/]+)/$', views.edit_user),
    url(r'user/delete/(?P<id>[^/]+)/$', views.del_user),
    url(r'user/change_password/(?P<id>[^/]+)/$', views.change_password),
    url(r'user/no_active/(?P<id>[^/]+)/$', views.no_active),
    url(r'user/active/(?P<id>[^/]+)/$', views.active),
)
