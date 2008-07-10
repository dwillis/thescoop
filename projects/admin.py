from django.contrib import admin
from thescoop.projects.models import Language, Project, Update, Presentation

class LanguageOptions(models.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class ProjectOptions(models.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class OrganizationOptions(models.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class TopicOptions(models.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Language, LanguageOptions)
admin.site.register(Project, ProjectOptions)
admin.site.register(Update)
admin.site.register(Presentation, PresentationOptions)
admin.site.register(Topic, TopicOptions)