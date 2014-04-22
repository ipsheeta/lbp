from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from pagemaker.views import TagView, UnsubscribeView
from feincms.module.page.sitemap import PageSitemap
from django.contrib import admin

admin.autodiscover()

sitemaps={'pages' : PageSitemap}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', TemplateView.as_view(template_name="youthSeed.html")),

    url(r'^hometest/$', TemplateView.as_view(template_name="ys_blog.html")),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^blog/', include('elephantblog.urls')),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    #url(r'^newsletter/', include('pennyblack.urls'), name='pennyblack'),
    #url(r'^newsletter/unsubscribe/$', UnsubscribeView.as_view(template_name='youthseed_unsubscribe/unsubscribe.html'), name='pennyblack'),
    #url(r'^newsletter/unsubscribe/confirm/$', TemplateView.as_view(template_name='youthseed_unsubscribe/thank_you.html'), name='confirm-unsubscribe'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('feincms.urls')),
    #url(r'^landing/', include('landingpage.urls')),
    # url(r'^ftwbrij/', include('ftwbrij.foo.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    # Uncomment the next line to enable the admin:
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                })
    )
