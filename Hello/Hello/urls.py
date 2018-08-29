from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wold/', include('Wold.urls')),
    url(r'^upload/', include('Nkx.urls')),
]
