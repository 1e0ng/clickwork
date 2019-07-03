from __future__ import absolute_import
from django.conf.urls import *

urlpatterns = patterns('user_management.views',
  (r'^$', 'change_password'),
  (r'^new/$', 'new_user'),
)
