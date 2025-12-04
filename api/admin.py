from django.contrib import admin
from .models import Project

# Customise how the list looks in admin panel
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at', 'updated_at')
    search_fields = ('title', 'technologies')

admin.site.register(Project, ProjectAdmin)
