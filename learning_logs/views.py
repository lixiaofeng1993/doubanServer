from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from learning_logs.forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'learing_logs/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    return render(request, 'learing_logs/topics.html', {'topics': topics})


@login_required
def topic(request, topic_id):
    """显示主题内容"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'learing_logs/topic.html', {'topic': topic, 'entries': entries})


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
        return HttpResponseRedirect(reverse('learning_logs:topics'))
    content = {'form': form}
    return render(request, 'learing_logs/new_topic.html', content)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    content = {'form': form, 'topic': topic}
    return render(request, 'learing_logs/new_entry.html', content)


@login_required
def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    return render(request, 'learing_logs/edit_entry.html', {'entry': entry, 'topic': topic, 'form': form})


def check_topic_owner(request, topic):
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
