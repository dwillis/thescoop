from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based, create_update
from thescoop.car.models import Byline, Datatype, Nation, Source, State, Story, Topic, Type
from thescoop.blog.models import Link, Category, Post
from thescoop.feeds import LatestEntries, LatestBylines, LatestSources, TopicFeed, SourceFeed, BylineFeed

info_dict = {
    'queryset': Story.objects.all().order_by('-pubdate'),
    'date_field':'pubdate',
}

post_dict = {
    'queryset': Post.objects.exclude(category__exact=22).order_by('-post_date'),
    'date_field':'post_date',
}

byline_list_info = {
	'queryset': Byline.objects.all().order_by('lastname'),
	'allow_empty': True,
	'paginate_by': 50,
	'template_name': 'byline_list.html',
}

feeds = {
    'latest': LatestEntries,
    'bylines': LatestBylines,
    'sources': LatestSources,
    'topic': TopicFeed,
    'source': SourceFeed,
    'byline': BylineFeed,
}


urlpatterns = patterns('',
    # Example:
    # (r'^thescoop/', include('thescoop.apps.foo.urls.foo')),

    (r'^feed/$', 'thescoop.car.views.blog_feed'),
    (r'^$', 'thescoop.car.views.blog_main'),

    (r'^docs/$', 'thescoop.car.views.main'),
    (r'^docs/story/(.*)/$', 'thescoop.car.views.story_detail'),
    (r'^docs/withdb/$', 'thescoop.car.views.with_db'),
    (r'^docs/type/$', 'thescoop.car.views.type_all'),
    (r'^docs/type/(.*)/$', 'thescoop.car.views.type_detail'),
    (r'^docs/datatype/$', 'thescoop.car.views.datatype_all'),
    (r'^docs/datatype/(.*)/$', 'thescoop.car.views.datatype_detail'),
    (r'^docs/topic/$', 'thescoop.car.views.topic_all'),
    (r'^docs/topic/(.*)/$', 'thescoop.car.views.topic_detail'),
    (r'^docs/byline/$', list_detail.object_list, byline_list_info),
    (r'^docs/search/byline/$', 'thescoop.car.views.byline_search'),
    (r'^docs/search/source/$', 'thescoop.car.views.source_search'),
    (r'^docs/byline/(.*)/$', 'thescoop.car.views.byline_detail'),
    (r'^docs/state/$', 'thescoop.car.views.state'),
    (r'^docs/state/(.*)/$', 'thescoop.car.views.state_detail'),
    (r'^docs/nation/$', 'thescoop.car.views.nation'),
    (r'^docs/nation/(.*)/$', 'thescoop.car.views.nation_detail'),
    (r'^docs/source/$', 'thescoop.car.views.source_main'),
    (r'^docs/source/(.*)/(\d+)/$', 'thescoop.car.views.source_by_year'),
    (r'^docs/source/(.*)/$', 'thescoop.car.views.source'),
    (r'^dbs/$', 'thescoop.car.views.db_index'),
    (r'^dbs/app/(?P<appslug>.*)/$', 'thescoop.car.views.db_app'),
    (r'^dbs/(.*)/$', 'thescoop.car.views.db_detail'),



    (r'^docs/date/$', 'django.views.generic.date_based.archive_index', dict(info_dict, template_name='story_archive_index.html')),
    (r'^docs/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', dict(info_dict, template_name='story_archive_year.html')),
    (r'^docs/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'django.views.generic.date_based.archive_month', dict(info_dict, template_name='story_archive_month.html')),
    (r'^docs/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'django.views.generic.date_based.archive_day', dict(info_dict, template_name='story_archive_day.html')),

    (r'^docs/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
