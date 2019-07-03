from __future__ import absolute_import
from django.conf import settings
from django.conf.urls import *
from django.contrib.auth.views import login, logout

from main.views import project, task, base, timesheets, overview, user
from main import wrapper

app_name = 'main'

urlpatterns = [
    url(r'^project/(?P<project_id>\d+)/api/(?P<url>.*)$', project.project_api),
    url(r'^task/(?P<task_id>\d+)/$', task.task_view, name='views.task.task_view'),
    url(r'^review/(?P<review_id>\d+)/$', task.task_review),
    url(r'^review/$', task.task_adhoc_review),
    url(r'^review/next/$', task.next_review),
    url(r'^next_task/', base.next_task),
    url(r'^abandon/', base.abandon_wip),
    url(r'^$', base.home),
    url(r'^about/$', base.about),
    url(r'^timesheet/', timesheets.timesheet),
    url(r'^projects/', overview.all_projects_brief),
    url(r'^projects-long/', overview.all_projects),
    url(r'^project/(\d+)/$', overview.one_project),
    url(r'^project/(\d+)/stats/$', project.project_stats),
    url(r'^project/(\d+)/agreement/$', project.project_agreement),
    url(r'^project/(\d+)/export/$', project.project_export),
    url(r'^project/(\d+)/upload/', project.project_upload),
    url(r'^groups/', overview.all_groups),
    url(r'^group/(\d+)/$', overview.one_group),
    url(r'^users/', overview.all_users),
    url(r'^user/([A-Za-z0-9@+._-]+)/$', overview.one_user),
    url(r'^user/([A-Za-z0-9@+._-]+)/responses/$', user.recent_responses),
    url(r'^user/([A-Za-z0-9@+._-]+)/results/$', user.recent_results),
    url(r'^remerge/(\d+)/$', task.unmerge),
    url(r'^wips/$', task.wip_review),
    url(r'^track/$', base.track_page_visit),
]

for task_type in settings.TASK_TYPES:
    mod = __import__("main.types.%s" % task_type, None, None, ["urlpatterns"])
    if hasattr(mod, "urlpatterns"):
        urlpatterns += [
            url("^project-type/%s/" % task_type.replace("_", "-"),
             include("main.types." + task_type)),
        ]

urlpatterns += [
    url(r"^wrap1/$", wrapper.smoke_test_1),
    url(r"^wrap2/$", wrapper.smoke_test_2),
]

urlpatterns += [
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/login/$', login),
]
