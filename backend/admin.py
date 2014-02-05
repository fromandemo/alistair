from django.contrib import admin
from backend.models import Project, Persona, ProjectDetail, Metadata, Category

class ProjectDetailInline(admin.StackedInline):
    model=ProjectDetail
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]
    list_display = ('name', 'status')
    
admin.site.register(Persona)
admin.site.register(Category)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Metadata)