from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length=50)
    nameslug = models.SlugField(prepopulate_from=('name',))
    class Admin:
        pass
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/docs/nation/%s/" % self.nameslug

class State(models.Model):
    abbrev = models.USStateField()
    statename = models.CharField(max_length=50)
    class Admin:
        pass
    def __str__(self):
        return self.abbrev
    def get_absolute_url(self):
        return "/docs/state/%s/" % self.abbrev.lower()

class Type(models.Model):
    typename = models.CharField(max_length=25)
    typeslug = models.SlugField(prepopulate_from=('typename',))
    class Admin:
        pass
    def __str__(self):
        return self.typename
    def get_absolute_url(self):
        return "/docs/type/%s/" % self.typeslug

class Source(models.Model):
    name = models.CharField(max_length=75)
    sourceslug = models.SlugField(prepopulate_from=('name',))
    state = models.ForeignKey(State, blank=True, null=True)
    nation = models.ForeignKey(Nation)
    type = models.ForeignKey(Type)
    class Admin:
        list_display = ('name', 'type', 'nation')
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/docs/source/%s/" % self.sourceslug

class Datatype(models.Model):
    datatype = models.CharField(max_length=50)
    dataslug = models.SlugField(prepopulate_from=('datatype',))
    class Admin:
        pass
    def __str__(self):
        return self.datatype
    def get_absolute_url(self):
        return "/docs/datatype/%s/" % self.dataslug

class Byline(models.Model):
    lastname = models.CharField(max_length=75)
    firstname = models.CharField(max_length=75)
    nameslug = models.SlugField(prepopulate_from=('firstname', 'lastname'))
    class Admin:
        ordering = ['lastname', 'firstname']
        search_fields = ['lastname']
    class Meta:
        ordering = ['lastname', 'firstname']
    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
    def full_name(self):
        return "%s, %s" % (self.lastname, self.firstname)
    def get_absolute_url(self):
        return "/docs/byline/%s/" % self.nameslug

class Topic(models.Model):
    topicname = models.CharField(max_length=50)
    topicslug = models.SlugField(prepopulate_from=('topicname',))
    class Admin:
        pass
    def __str__(self):
        return self.topicname
    def get_absolute_url(self):
        return "/docs/topic/%s/" % self.topicslug

class Story(models.Model):
    pubdate = models.DateField(null=True,blank=True)
    postdate = models.DateField()
    source = models.ForeignKey(Source)
    url = models.URLField()
    byline = models.ManyToManyField(Byline, filter_interface=models.VERTICAL, blank=True)
    headline = models.CharField(max_length=90)
    headslug = models.SlugField(prepopulate_from=('headline',))
    datatype = models.ManyToManyField(Datatype)
    topic = models.ManyToManyField(Topic, null=True)
    methodology = models.CharField(max_length=90, null=True, blank=True)
    dburl = models.URLField(null=True, blank=True)
    description = models.TextField()
    note = models.TextField(null=True, blank=True)
    class Admin:
        list_display = ('headline', 'source', 'pubdate')
        search_fields = ['headline']
    def __str__(self):
        return "%s, %s (%s)" % (self.headline, self.source, self.postdate)
    def get_absolute_url(self):
        return "/docs/story/%s/" % self.headslug
    def has_db(self):
        if self.dburl == None:
            return False
        else:
            return True
    def file_type(self):
        return self.dburl.split('.')[-1]
    class Meta:
        verbose_name_plural='Stories'

class Application(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(prepopulate_from=('name',))
    
    class Admin:
        pass
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/dbs/app/%s/" % self.slug

class Database(models.Model):
    post_date = models.DateField(blank=True)
    source = models.ForeignKey(Source)
    url = models.URLField()
    title = models.CharField(max_length=90)
    slug = models.SlugField(prepopulate_from=('title',))
    credit = models.ManyToManyField(Byline, filter_interface=models.VERTICAL, blank=True)
    topic = models.ManyToManyField(Topic, null=True)
    application = models.ForeignKey(Application)
    description = models.TextField()
    
    class Admin:
        pass
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/dbs/%s/" % self.slug