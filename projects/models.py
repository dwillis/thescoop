from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(prepopulate_from=('name',))
    
    def __unicode__(self):
        return self.name
    
    class Admin:
        pass

class Project(models.Model):
    title = models.CharField(max_length=90)
    language = models.ForeignKey(Language)
    repository_url = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    changes_feed_url = models.CharField(max_length=120, blank=True)
    updated = models.DateField()

    def __unicode__(self):
        return self.title
    
    class Admin:
        pass
    