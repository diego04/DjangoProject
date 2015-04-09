from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheIsland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'LandingPage.views.login'),
    url(r'^home/$', 'LandingPage.views.home'),
    url(r'^logout/$', 'LandingPage.views.logout'),

)
