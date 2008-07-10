from django.contrib import admin
from thescoop.car.models import Byline, Datatype, Nation, Source, State, Story, Topic, Type, Application, Database

class SourceOptions(admin.ModelAdmin):
    list_display = ('name', 'type', 'nation')
    ordering = ['name']
    prepopulated_fields = {'sourceslug': ('name',)}

class BylineOptions(admin.ModelAdmin):
    ordering = ['lastname', 'firstname']
    search_fields = ['lastname']
    prepopulated_fields = {'nameslug': ('firstname', 'lastname')}

class StoryOptions(admin.ModelAdmin):
    list_display = ('headline', 'source', 'pubdate')
    search_fields = ['headline']
    prepopulated_fields = {'headslug': ('headline',)}
    date_hierarchy = 'pubdate'
    filter_vertical = ('byline', 'topic')

class NationOptions(admin.ModelAdmin):
    prepopulated_fields = {'nameslug' : ('name',)}

class TypeOptions(admin.ModelAdmin):
    prepopulated_fields = {'typeslug' : ('typename',)}

class DatatypeOptions(admin.ModelAdmin):
    prepopulated_fields = {'dataslug' : ('datatype',)}

class TopicOptions(admin.ModelAdmin):
    prepopulated_fields = {'topicslug' : ('topicname',)}

class ApplicationOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class DatabaseOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    filter_vertical = ('credit',)

admin.site.register(Source, SourceOptions)
admin.site.register(Byline, BylineOptions)
admin.site.register(Story, StoryOptions)
admin.site.register(Nation, NationOptions)
admin.site.register(State)
admin.site.register(Type, TypeOptions)
admin.site.register(Datatype, DatatypeOptions)
admin.site.register(Topic, TopicOptions)
admin.site.register(Application, ApplicationOptions)
admin.site.register(Database, DatabaseOptions)