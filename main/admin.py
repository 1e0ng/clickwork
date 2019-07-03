from __future__ import absolute_import
from django.contrib import admin
from main.models import Project, ProjectTag, ProjectTagAdmin, ProjectAdmin, ProjectUpload, Announcement

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTag, ProjectTagAdmin)
admin.site.register(ProjectUpload)
admin.site.register(Announcement)
