# !/usr/bin/env python
# coding=utf-8
import json

import requests
from django.core.cache import cache
from django.conf import settings
from redis import Redis
import random
from douban.models import MovieHome, MusicHome, BookHome
r = Redis(**settings.REDIS)


def page_cache(timeout):
    def wrap1(view_func):  # page_cache装饰器
        def wrap2(request, *args, **kwargs):
            key = 'Response-{}'.format(request.get_full_path())     # 拼接唯一的key
            response = cache.get(key)   # 从缓存中获取数据
            print('从缓存中获取数据:{}'.format(response))
            # 添加阅读计数
            if response is None:
                # 获取数据库中的数据,在添加到缓存中
                response = view_func(request, *args, **kwargs)
                cache.set(key, response, timeout)
                print('从数据库中获取:{}'.format(response))
            return response
        return wrap2
    return wrap1


def get_top_n(n, top_func):
    '''获取 Top N'''
    if top_func == 'movie_top10':
        rank_data = r.zrevrange('ReadRank--movie', 0, n - 1, withscores=True)
    if top_func == 'book_top10':
        rank_data = r.zrevrange('ReadRank--book', 0, n - 1, withscores=True)
    if top_func == 'music_top10':
        rank_data = r.zrevrange('ReadRank--music', 0, n - 1, withscores=True)
    rank_data = [[int(post_id), int(num)] for post_id, num in rank_data]
    post_id_list = [d[0] for d in rank_data]
    if top_func == 'movie_top10':
        posts = {post.movieId: post for post in MovieHome.objects.filter(movieId__in=post_id_list)}
    if top_func == 'book_top10':
        posts = {post.book_id: post for post in BookHome.objects.filter(book_id__in=post_id_list)}
    if top_func == 'music_top10':
        posts = {post.music_id: post for post in MusicHome.objects.filter(music_id__in=post_id_list)}
    rank_data = [[posts[post_id], num] for post_id, num in rank_data]
    return rank_data


def gen_random_code(n):
    """生成n位数的验证码"""
    return random.randint(10 ** (n - 1), 10 ** n - 1)


def send_phone_code(phone):
    code = gen_random_code(6)
    r.set('CODE-{}'.format(phone), code, 60)
    data = settings.SMS.copy()
    data['content'] = data['content'] % code
    data['mobile'] = phone
    resp = requests.post(settings.SMS_URL, data, settings.SMS_HEADERS)
    if json.loads(resp.text).get('code') != 2:
        raise ValueError('验证码发送失败!')
    else:
        return True


def check_code(phone, code):
    code0 = int(r.get('CODE-{}'.format(phone)))
    code = int(code)
    return code0 == code