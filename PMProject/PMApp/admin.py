from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Project, Task

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name']
    date_hierarchy = 'creation_time'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('description',)
    search_fields = ['title']



admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
