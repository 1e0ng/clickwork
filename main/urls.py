from __future__ import absolute_import
from django.conf import settings
from django.conf.urls import *
import django.contrib.auth.views as auth_views

from main.views import project, task, base, timesheets, overview, user
from main import wrapper

app_name = 'main'

urlpatterns = [
    url(
        r'^project/(?P<project_id>\d+)/api/(?P<url>.*)$',
        project.project_api,
        name='project-api',
    ),
    url(r'^task/(?P<task_id>\d+)/$', task.task_view, name='view-task'),
    url(r'^review/(?P<review_id>\d+)/$', task.task_review, name='view-review'),
    url(r'^review/$', task.task_adhoc_review, name='review'),
    url(r'^review/next/$', task.next_review, name='next-review'),
    url(r'^next_task/', base.next_task, name='next-task'),
    url(r'^abandon/', base.abandon_wip, name='abandon'),
    url(r'^$', base.home, name='home'),
    url(r'^about/$', base.about, name='about'),
    url(r'^timesheet/', timesheets.timesheet, name='timesheet'),
    url(r'^projects/', overview.all_projects_brief, name='project-list'),
    url(r'^projects-long/', overview.all_projects, name='all-project-list'),
    url(r'^project/(\d+)/$', overview.one_project, name='view-project'),
    url(r'^project/(\d+)/stats/$', project.project_stats, name='view-project-stats'),
    url(
        r'^project/(\d+)/agreement/$',
        project.project_agreement,
        name='view-project-agreement',
    ),
    url(r'^project/(\d+)/export/$', project.project_export, name='view-project-export'),
    url(r'^project/(\d+)/upload/', project.project_upload, name='view-project-upload'),
    url(r'^groups/', overview.all_groups, name='group-list'),
    url(r'^group/(\d+)/$', overview.one_group, name='view-group'),
    url(r'^users/', overview.all_users, name='user-list'),
    url(r'^user/([A-Za-z0-9@+._-]+)/$', overview.one_user, name='view-user'),
    url(
        r'^user/([A-Za-z0-9@+._-]+)/responses/$',
        user.recent_responses,
        name='user-response-list',
    ),
    url(
        r'^user/([A-Za-z0-9@+._-]+)/results/$',
        user.recent_results,
        name='user-result-list',
    ),
    url(r'^remerge/(\d+)/$', task.unmerge, name='remerge'),
    url(r'^wips/$', task.wip_review, name='wip-list'),
    url(r'^track/$', base.track_page_visit, name='track'),
]

for task_type in settings.TASK_TYPES:
    mod = __import__("main.types.%s" % task_type, None, None, ["urlpatterns"])
    if hasattr(mod, "urlpatterns"):
        urlpatterns += [
            url(
                "^project-type/%s/" % task_type.replace("_", "-"),
                include("main.types." + task_type),
            )
        ]

urlpatterns += [
    url(r"^wrap1/$", wrapper.smoke_test_1),
    url(r"^wrap2/$", wrapper.smoke_test_2),
]

urlpatterns += [
    url(
        r'^accounts/logout/$',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout',
    ),
    url(
        r'^accounts/login/$',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
]
