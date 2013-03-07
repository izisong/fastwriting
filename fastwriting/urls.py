#encoding=utf-8
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^sitemedia/(?P<path>.*)','django.views.static.serve',{'document_root':'/home/liyasong/website/fastwriting/fastwriting/static'}),
)

urlpatterns += patterns('fastwriting.views',
    # Examples:
    # url(r'^$', 'fastwriting.views.home', name='home'),
    # url(r'^fastwriting/', include('fastwriting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('fastwriting.writing.views',
    (r'^$', 'index'),
    (r'^index/$', 'index'),
    (r'^design-style/$', 'design_style'),
    (r'^import-blog/$', 'import_blog'),
    (r'^deal-blog/$', 'deal_blog'),
    (r'^fast-writing/$', 'fast_writing'),
	#(r'^match/\w+/$', 'match'),
	(r'^match/(?P<style_name>\w+)/(?P<sentence>.+)/$', 'match'),
	(r'^test/(?P<style_name>\w+)/(?P<sentence>\S+)/$', 'test'),
)
