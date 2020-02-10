from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.defaults import page_not_found, server_error
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.feeds import BlogIndexFeedRSS, BlogIndexFeedAtom

urlpatterns = [
    url(r'^blog/feed/rss/$', BlogIndexFeedRSS(), name='blog_rss'),
    url(r'^blog/feed/atom/$', BlogIndexFeedAtom(), name='blog_atom'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^400/$', TemplateView.as_view(template_name='400.html')),
        url(r'^403/$', TemplateView.as_view(template_name='403.html')),
        url(r'^404/$', page_not_found),
        url(r'^500/$', server_error),
        url(r'^styleguide/$', TemplateView.as_view(template_name='core/styleguide.html')),
        url(r'^styleguide/components/$', TemplateView.as_view(template_name='core/components.html')),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
