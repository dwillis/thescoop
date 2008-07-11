from django.contrib import admin
from thescoop.projects.models import Language, Project, Update, Presentation

class LanguageOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class ProjectOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class OrganizationOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class TopicOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Language, LanguageOptions)
admin.site.register(Project, ProjectOptions)
admin.site.register(Update)
admin.site.register(Presentation)
admin.site.register(Topic, TopicOptions)