from django.conf.urls import url
from . import views


urlpatterns = [
    # 首页
    url(r'^$', view=views.index, name='index'),
    url(r'^topics/$', view=views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', view=views.topic, name='topic'),
    url(r'^new_topic/$', view=views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', view=views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', view=views.edit_entry, name='edit_entry'),
]
