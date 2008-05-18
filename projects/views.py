from thescoop.projects.models import Language, Project, Update
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.syndication.feeds import Feed
import feedparser
import datetime

def index(request):
    project_list = Project.objects.all().select_related().order_by('title')
    recent_updates = Update.objects.all().order_by('-date')[:5]
    return render_to_response('projects/index.html', {'project_list': project_list, 'recent_updates': recent_updates})

def language_list(request, lang):
    language = get_object_or_404(Language, slug=lang)
    project_list = Project.objects.filter(language=language).order_by('title')
    return render_to_response('projects/language.html', {'language': language, 'project_list': project_list})

def project_detail(request, project):
    project = get_object_or_404(Project, slug=project)
    updates = Update.objects.filter(project=project).order_by('-date')
    feed = feedparser.parse(project.changes_feed_url)
    for item in feed.entries:
        item.date = datetime.date(item.updated_parsed[0], item.updated_parsed[1], item.updated_parsed[2])
    return render_to_response('projects/project_detail.html', {'project': project, 'feed': feed, 'updates': updates})

def presentations(request):
    pass