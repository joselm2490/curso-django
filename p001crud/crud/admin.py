from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created')
    list_filter = ('is_completed', 'created')
    search_fields = ('title', 'description')
    ordering = ('-created',)
