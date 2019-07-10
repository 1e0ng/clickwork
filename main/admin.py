from __future__ import absolute_import
from django.contrib import admin
from main import models

admin.site.register(models.Project, models.ProjectAdmin)
admin.site.register(models.ProjectTag, models.ProjectTagAdmin)
admin.site.register(models.ProjectUpload)
admin.site.register(models.Announcement)
admin.site.register(models.Task)
