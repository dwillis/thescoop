from thescoop.car.models import Byline, Datatype, Nation, Source, State, Story, Topic, Type, Application, Database
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.syndication.feeds import Feed

def main(request):
	recent_stories = Story.objects.all().order_by('-postdate')[:5]
	return render_to_response('index.html', {'recent_stories': recent_stories})

def with_db(request):
	db_stories = Story.objects.filter(dburl__istartswith='http').order_by('-postdate')[:25]
	return render_to_response('withdb.html', {'db_stories': db_stories})

def byline_main(request):
	recent_bylines = Byline.objects.all().order_by('-id')[:15]
	return render_to_response('byline.html', {'recent_bylines': recent_bylines})

def byline_detail(request, byslug):
	story_list = Story.objects.select_related().filter(byline__nameslug__exact=byslug).order_by('-pubdate')
	byline_name = Byline.objects.get(nameslug__exact=byslug)
	return render_to_response('byline_detail.html', {'story_list': story_list, 'name': byline_name, 'nameslug': byslug})

def state(request):
	state_list = State.objects.all().order_by('statename')
	return render_to_response('state.html', {'state_list': state_list})

def state_detail(request, state):
    s = get_object_or_404(State, abbrev=state.upper())        
    state_list = Source.objects.filter(state=s).order_by('name')
    story_list = Story.objects.select_related().filter(source__state=s).order_by('-pubdate')[:10]
    return render_to_response('state_detail.html', {'state_list': state_list, 'state': s, 'story_list': story_list})

def source_main(request):
	source_list = Source.objects.extra(select={'source_count': 'SELECT COUNT(*) FROM car_story WHERE car_story.source_id=car_source.id HAVING COUNT(*)>0'},).order_by('name')
	return render_to_response('source_main.html', {'source_list': source_list})

def source(request, sourceslug):
    try:
        source = get_object_or_404(Source, sourceslug=sourceslug)
        source_list = Story.objects.select_related().filter(source=source).order_by('-pubdate')
        year_list = source_list.dates('pubdate', 'year')[::-1]
        byline_list = []
        for story in source_list:
            for byline in story.byline.all().order_by('car_byline.lastname'):
                if byline in byline_list:
                    pass
                else:
                    byline_list.append(byline)
        byline_list.sort()
        topic_list = []
        for story in source_list:
            for topic in story.topic.all():
                if topic in topic_list:
                    pass
                else:
                    topic_list.append(topic)
        topic_list.sort()
        return render_to_response('source.html', {'source_list': source_list, 'year_list': year_list, 'source':source, 'sourceslug': sourceslug, 'story_num': len(source_list), 'byline_list': byline_list, 'topic_list': topic_list})
    except IndexError:
        raise Http404

def source_by_year(request, sourceslug, year):
	source_list = Story.objects.select_related().filter(source__sourceslug__exact=sourceslug, pubdate__year=year).order_by('-pubdate')
	return render_to_response('source_year.html', {'source_list': source_list, 'source_name':source_list[0].source, 'sourceslug': sourceslug, 'year': year})

def byline_all(request):
	all_bylines = Byline.objects.all().order_by('lastname')
	return render_to_response('byline.html', {'all_bylines': all_bylines})

def topic_all(request):
	all_topics = Topic.objects.all().order_by('topicname')
	return render_to_response('topic.html', {'all_topics': all_topics})

def topic_detail(request, topslug):
	story_list = Story.objects.select_related().filter(topic__topicslug__exact=topslug).order_by('-pubdate')
	topic_name = Topic.objects.get(topicslug__exact=topslug)
	return render_to_response('topic_detail.html', {'story_list': story_list, 'name': topic_name, 'topslug': topslug})

def datatype_all(request):
	all_datatypes = Datatype.objects.all().order_by('datatype')
	return render_to_response('datatype.html', {'all_datatypes': all_datatypes})

def datatype_detail(request, dtslug):
	story_list = Story.objects.select_related().filter(datatype__dataslug__exact=dtslug).order_by('-pubdate')
	datatype_name = Datatype.objects.get(dataslug__exact=dtslug)
	return render_to_response('datatype_detail.html', {'story_list': story_list, 'name': datatype_name})

def nation(request):
	nation_list = Nation.objects.all().order_by('name')
	return render_to_response('nation.html', {'nation_list': nation_list})

def nation_detail(request, natslug):
    try:
        nation_list = Source.objects.filter(nation__nameslug__exact=natslug).order_by('name')
        return render_to_response('nation_detail.html', {'nation_list': nation_list, 'nation': nation_list[0].nation.name})
    except IndexError:
        raise Http404

def type_all(request):
	all_types = Type.objects.all().order_by('typename')
	return render_to_response('type.html', {'all_types': all_types})

def type_detail(request, typslug):
	story_list = Story.objects.select_related().filter(source__type__typeslug__exact=typslug).order_by('-pubdate')[:50]
	type_name = Type.objects.get(typeslug__exact=typslug)
	return render_to_response('type_detail.html', {'story_list': story_list, 'name': type_name})

def story_detail(request, storyslug):
	story = Story.objects.select_related().get(headslug__exact=storyslug)
	bylines = story.byline.all()
	topics = story.topic.all()
	datatypes = story.datatype.all()
	return render_to_response('story_detail.html', {'story': story, 'bylines': bylines, 'topics': topics, 'datatypes': datatypes})

def byline_search(request):
	search_results = Byline.objects.select_related().filter(lastname__icontains=request.POST['term']).order_by('lastname')
	return render_to_response('byline_search.html',{'search_results':search_results, 'term':request.POST['term']})

def source_search(request):
	search_results = Source.objects.select_related().filter(name__icontains=request.POST['term']).order_by('name')
	return render_to_response('source_search.html',{'search_results':search_results, 'term':request.POST['term']})

def blog_feed(request):
	return HttpResponseRedirect('http://blog.thescoop.org/feed/')

def blog_main(request):
    return HttpResponseRedirect('http://blog.thescoop.org/')

def db_index(request):
    recent_dbs = Database.objects.all().order_by('-post_date')[:5]
    app_types = Applications.objects.all().order_by('name')
    return render_to_response('db_index.html', {'recent_dbs': recent_dbs, 'app_types': app_types})

def db_detail(request, slug):
    db = get_object_or_404(Database, slug=slug)
    credits = db.credit.all()
    topics = db.topic.all()
    return render_to_response('db_detail.html', {'database': db, 'credits': credits, 'topics': topics })

def db_app(request, appslug):
    app = get_object_or_404(Application, slug=appslug)
    db_list = get_list_or_404(Database, application=app).order_by('-post_date')
    return render_to_response('db_app.html', {'app': app, 'db_list': db_list })