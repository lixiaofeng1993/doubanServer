# !/usr/bin/env python
# coding=utf-8
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    # 首页
    url(r'^$', view=views.home),
    # movie
    url(r'^movie/(\d{1,2})/$', view=views.movie),
    url(r'^movie/(\d+)/$', view=views.movie_info),
    url(r'^movie/(\d+)/comments/$', view=views.movie_comments),
    url(r'^movie/(\d+)/read/$', view=views.movie_read),
    url(r'^movie/top10/', view=views.movie_top10),
    # book
    url(r'^book/(\d{1,2})/$', view=views.book),
    url(r'^book/(\d+)/$', view=views.book_info),
    url(r'^book/(\d+)/comments/$', view=views.book_comments),
    url(r'^book/(\d+)/read/$', view=views.book_read),
    url(r'^book/top10/', view=views.book_top10),
    # music
    url(r'^music/(\d{1,2})/$', view=views.music),
    url(r'^music/(\d+)/$', view=views.music_info),
    url(r'^music/(\d+)/comments/$', view=views.music_comments),
    url(r'^music/(\d+)/read/$', view=views.music_read),
    url(r'^music/top10/', view=views.music_top10),

    url(r'^login/$', view=views.login_user),
    url(r'^user/info/$', view=views.user_info),
    url(r'^register/$', view=views.register),
    url(r'^quit/$', view=views.quit),
    url(r'^what/$', view=views.what),
    url(r'^code/$', view=views.code_login),
    url(r'^send/$', view=views.send_code),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
