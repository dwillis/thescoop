from django.contrib.syndication.feeds import Feed
from thescoop.car.models import Byline, Datatype, Nation, Source, State, Story, Topic, Type

class LatestEntries(Feed):
	title = "The Scoop DOCS Recent Stories Feed"
	link = "/docs/"
	description = "Most recent stories posted to DOCS"

	def items(self):
		return Story.objects.select_related().order_by('-postdate')[:10]

class LatestBylines(Feed):
	title = "The Scoop DOCS Recent Bylines Feed"
	link = "/docs/"
	description = "Most recent bylines posted to DOCS"

	def items(self):
		return Byline.objects.order_by('-id')[:15]

class LatestSources(Feed):
	title = "The Scoop DOCS Recent Sources Feed"
	link = "/docs/"
	description = "Most recent sources posted to DOCS"

	def items(self):
		return Source.objects.order_by('-id')[:10]

class TopicFeed(Feed):
	def get_object(self, bits):
#		if len(bits) != 1:
#			raise ObjectDoesNotExist
		return Topic.objects.get(topicslug__exact=bits[0])

	def title(self, obj):
		return "The Scoop DOCS: Stories on %s" % obj.topicname

	def link(self, obj):
		return obj.get_absolute_url()

	def description(self, obj):
		return "Stories recently added on %s" % obj.topicname

	def items(self, obj):
		return Story.objects.select_related().filter(topic__topicslug__exact=obj.topicslug).order_by('-pubdate')[:15]

class SourceFeed(Feed):
	def get_object(self, bits):
		return Source.objects.get(sourceslug__exact=bits[0])

	def title(self, obj):
		return "The Scoop DOCS: Stories from %s" % obj.name

	def link(self, obj):
		return obj.get_absolute_url()

	def description(self, obj):
		return "Stories recently added on %s" % obj.name

	def items(self, obj):
		return Story.objects.select_related().filter(source__sourceslug__exact=obj.sourceslug).order_by('-pubdate')[:15]

class BylineFeed(Feed):
	def get_object(self, bits):
		return Byline.objects.get(nameslug__exact=bits[0])

	def title(self, obj):
		return "The Scoop DOCS: Stories by %s" % obj

	def link(self, obj):
		return obj.get_absolute_url()

	def description(self, obj):
		return "Recently added stories by %s" % obj

	def items(self, obj):
		return Story.objects.select_related().filter(byline__nameslug__exact=obj.nameslug).order_by('-pubdate')[:15]
