from __future__ import absolute_import
from django.conf.urls import url, include
from django.views.static import serve

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(
        r'^favicon.ico',
        serve,
        {'document_root': 'clickwork/static', 'path': 'favicon.ico'},
    ),
    url(r'^user_management/', include('user_management.urls')),
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
]
