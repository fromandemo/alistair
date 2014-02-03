from django.contrib import admin
from backend.models import Project, Persona, ProjectDetail, CarouselItem, Metadata, Category

class ProjectDetailInline(admin.StackedInline):
    model=ProjectDetail
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]
    list_display = ('name', 'status')

class CarouselAdmin(admin.ModelAdmin):
    list_display =('title','position',)
    
admin.site.register(Persona)
admin.site.register(Category)
admin.site.register(Project,ProjectAdmin)
admin.site.register(CarouselItem,CarouselAdmin)
admin.site.register(Metadata)