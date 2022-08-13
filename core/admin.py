from django.contrib import admin
from core.models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'updated_at', 'tasker')
    list_filter = ('completed',)
    search_fields = ('name',)
    ordering = ('-updated_at',)
    fields = ('name', 'description', 'completed', 'tasker','id', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

