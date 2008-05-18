from django.db import models

LINK_CATEGORIES = (
    ('A', 'Around the Site'),
    ('S', 'Sources'),
    ('P', 'People'),
    ('M', 'Methods'),
)

ENTRY_CHOICES = (
    ('P', 'Entry'),
    ('S', 'Essay'),
    ('M', 'Methods'),
)

class Link(models.Model):
    id = models.IntegerField(db_column="link_id", primary_key=True)
    url = models.URLField(db_column="link_url")
    title = models.CharField(db_column="link_name", max_length=90)
    category = models.IntegerField(max_length=1, choices=LINK_CATEGORIES)
    def __str__(self):
        return self.title
    class Admin:
        list_display = ('title', 'url', 'category')

class Category(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=90)
	nameslug = models.SlugField(prepopulate_from=('name',))
	class Admin:
		pass
	class Meta:
		verbose_name_plural = 'Categories'

class Post(models.Model):
	def __str__(self):
		return self.title
	post_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	titleslug = models.SlugField(prepopulate_from=('title',))
	type = models.CharField(max_length=1, choices=ENTRY_CHOICES)
	category = models.ManyToManyField(Category)
	excerpt = models.CharField(max_length=255, blank=True)
	contents = models.TextField()
	update_date = models.DateTimeField(auto_now=True, editable=False)
	class Admin:
		list_display = ('title', 'excerpt', 'type', 'post_date', 'update_date')
		search_fields = ['title', 'contents']