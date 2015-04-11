from django.conf.urls import patterns, include, url
from django.contrib import admin

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

from django.conf.urls import patterns, url

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheIsland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'LandingPage.views.login'),
    url(r'^home/$', 'LandingPage.views.home'),
    url(r'^logout/$', 'LandingPage.views.logout'),


    #(r'^comments/', include('django_comments.urls')),

    #url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    #url(r'^comments/', include('django_comments.urls')),
    url(r"^blog/", include("pinax.blog.urls")),

)

