from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=90)
    slug = models.SlugField()
    language = models.ForeignKey(Language)
    repository_url = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    changes_feed_url = models.CharField(max_length=120, blank=True)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/code/%s/" % self.slug

class Update(models.Model):
    project = models.ForeignKey(Project)
    date = models.DateField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title

class Organization(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

class Presentation(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    organization = models.ForeignKey(Organization)
    topic = models.ForeignKey(Topic)
    date = models.DateField()
    text = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title