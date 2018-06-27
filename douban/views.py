from django.shortcuts import render, redirect
from .models import MovieInfo, MovieHome, MovieComment, BookInfo, BookHome, BookComment, MusicInfo, MusicHome, \
    MusicComment, User, What
from django.contrib.auth.hashers import check_password, make_password
from douban.form import RegisterForm
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth import logout, authenticate, login
import time
from douban.helper import page_cache, r, get_top_n, send_phone_code, check_code


@page_cache(2)
def home(request):
    movie_name = MovieHome.objects.all()[0:7]
    book_name = BookHome.objects.all()[0:7]
    music_name = MusicHome.objects.all()[0:7]
    return render(request, 'home.html', {'movie_name': movie_name, 'book_name': book_name, 'music_name': music_name})


@page_cache(2)
def movie(request, pid):
    data_list = MovieHome.objects.all()
    paginator = Paginator(data_list, 20)
    movies = paginator.page(pid)
    return render(request, 'movie/movie.html', {'data': movies})


def movie_info(request, mid):
    movie_name = MovieHome.objects.filter(movieId=mid)
    data = MovieInfo.objects.filter(movieId=mid)
    content = MovieComment.objects.filter(movieId=mid)[0:5]
    r.zincrby('ReadRank--movie', mid)
    return render(request, 'movie/movie_info.html', {'data': data, 'movieName': movie_name, 'content': content})


@page_cache(2)
def movie_comments(request, mid):
    movie_name = MovieHome.objects.filter(movieId=mid)
    data = MovieComment.objects.filter(movieId=mid)
    if request.method == 'GET':
        return render(request, 'movie/movie_comments.html', {'data': data, 'movieName': movie_name})
    else:
        states = request.POST.get('states')
        content = request.POST.get('content')
        content_time = time.strftime('%Y-%m-%d')
        movie_id = mid
        uid = request.session.get('uid')
        user = User.objects.get(id=uid)
        net_name = user.net_name
        net_img = '/media/' + str(user.net_img)
        movie_comment = MovieComment.create_comment(netName=net_name, movieId=movie_id, movieName='', states=states,
                                                    content=content, contentTime=content_time, comment_website='',
                                                    netImg=net_img)
        movie_comment.save()
        return render(request, 'movie/movie_comments.html', {'data': data, 'movieName': movie_name})


@page_cache(2)
def movie_read(request, mid):
    data = MovieHome.objects.filter(movieId=mid)
    if request.method == 'GET':
        if request.session.get('uid'):
            return render(request, 'movie/movie_read.html', {'data': data})
        else:
            return render(request, 'user/login.html')


def movie_top10(request):
    top10 = get_top_n(15, 'movie_top10')
    return render(request, 'movie/movie_top10.html', {'top10': top10})


@page_cache(2)
def book(request, pid):
    data_list = BookHome.objects.all()
    paginator = Paginator(data_list, 20)
    books = paginator.page(pid)
    return render(request, 'book/book.html', {'data': books})


def book_info(request, mid):
    book_name = BookHome.objects.filter(book_id=mid)
    data = BookInfo.objects.filter(book_id=mid)
    content = BookComment.objects.filter(book_id=mid)[0:5]
    r.zincrby('ReadRank--book', mid)
    return render(request, 'book/book_info.html', {'data': data, 'book_name': book_name, 'content': content})


@page_cache(2)
def book_comments(request, mid):
    book_name = BookHome.objects.filter(book_id=mid)
    data = BookComment.objects.filter(book_id=mid)
    if request.method == 'GET':
        return render(request, 'book/book_comments.html', {'data': data, 'book_name': book_name})
    else:
        states = request.POST.get('states')
        content = request.POST.get('content')
        content_time = time.strftime('%Y-%m-%d')
        uid = request.session.get('uid')
        user = User.objects.get(id=uid)
        net_name = user.net_name
        net_img = '/media/' + str(user.net_img)
        book_id = mid
        book_comment = BookComment.create_comment(net_name=net_name, book_id=book_id, book_name='', states=states,
                                                  content=content, contentTime=content_time, book_comment_website='',
                                                  net_img=net_img)
        book_comment.save()
        return render(request, 'book/book_comments.html', {'data': data, 'book_name': book_name})


@page_cache(2)
def book_read(request, mid):
    data = BookHome.objects.filter(book_id=mid)
    if request.method == 'GET':
        if request.session.get('uid'):
            return render(request, 'book/book_read.html', {'data': data})
        else:
            return render(request, 'user/login.html')


def book_top10(request):
    top10 = get_top_n(15, 'book_top10')
    return render(request, 'book/book_top10.html', {'top10': top10})


@page_cache(2)
def music(request, pid):
    data_list = MusicHome.objects.all()
    paginator = Paginator(data_list, 30)
    musics = paginator.page(pid)
    return render(request, 'music/music.html', {'data': musics})


def music_info(request, mid):
    music_name = MusicHome.objects.filter(music_id=mid)
    data = MusicInfo.objects.filter(music_id=mid)
    content = MusicComment.objects.filter(music_id=mid)[0:5]
    r.zincrby('ReadRank--music', mid)
    return render(request, 'music/music_info.html', {'data': data, 'music_name': music_name, 'content': content})


@page_cache(2)
def music_comments(request, mid):
    music_name = MusicHome.objects.filter(music_id=mid)
    data = MusicComment.objects.filter(music_id=mid)
    if request.method == 'GET':
        return render(request, 'music/music_comments.html', {'data': data, 'music_name': music_name})

    else:
        states = request.POST.get('states')
        content = request.POST.get('content')
        content_time = time.strftime('%Y-%m-%d')
        uid = request.session.get('uid')
        user = User.objects.get(id=uid)
        net_name = user.net_name
        net_img = '/media/' + str(user.net_img)
        music_id = mid
        music_comment = MusicComment.create_comment(net_name=net_name, music_id=music_id, music_name='', states=states,
                                                    content=content, contentTime=content_time,
                                                    music_comment_website='', net_img=net_img)
        music_comment.save()
        return render(request, 'music/music_comments.html', {'data': data, 'music_name': music_name})


@page_cache(2)
def music_read(request, mid):
    data = MusicHome.objects.filter(music_id=mid)
    if request.method == 'GET':
        if request.session.get('uid'):
            return render(request, 'music/music_read.html', {'data': data})
        else:
            return render(request, 'user/login.html')


def music_top10(request):
    top10 = get_top_n(15, 'music_top10')
    return render(request, 'music/music_top10.html', {'top10': top10})


def login_user(request):
    if request.method == 'GET':
        # 把来源的url保存到session中
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'user/login.html')
    else:
        userPhone = request.POST.get('userPhone')
        password = request.POST.get('userPass')
        try:
            user = User.objects.get(phone=userPhone)
            if not check_password(password, user.password):
                return render(request, 'user/login.html', {'error': '密码错误!!'})
            else:
                # 跳转到点击登录的界面
                response = redirect(request.session['login_from'])
                # 状态保持
                request.session['net_name'] = user.net_name
                request.session['uid'] = user.id
                return response
        except User.DoesNotExist as e:
            return render(request, 'user/login.html', {'error': '用户名错误!!'})


def user_info(request):
    uid = request.session.get('uid')
    if uid:
        user = User.objects.get(id=uid)
        return render(request, 'user/user_info.html', {'user': user})
    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            request.session['uid'] = user.id
            request.session['net_name'] = user.net_name
            response = redirect(request.session['login_from'])
            return response
        else:
            return render(request, 'user/register.html', {'error': form.errors})


def quit(request):
    login_from = request.META.get('HTTP_REFERER', '/')
    response = redirect(login_from)
    request.session.flush()
    return response


def what(request):
    if request.method == 'GET':
        if request.session.get('uid'):
            return render(request, 'what.html')
        else:
            request.session['login_from'] = 'http://longlove.wang/what/'
            return render(request, 'user/login.html')
    else:
        content = request.POST.get('content')
        net_name = request.session.get('net_name')
        phone = User.objects.get(net_name=net_name).phone
        word = What.create_comment(net_name=net_name, content=content, phone=phone)
        word.save()
        return redirect('/')


def code_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        try:
            user = User.objects.get(phone=phone)
            if check_code(phone, code):
                # 状态保持
                request.session['net_name'] = user.net_name
                request.session['uid'] = user.id
                return redirect('/')
        except User.DoesNotExist as e:
            return render(request, 'user/code_login.html', {'error': '手机号未注册,请先注册!'})
    return render(request, 'user/code_login.html')


def send_code(request):
    phone = request.POST.get('userPhone')
    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist as e:
        return render(request, 'user/code_login.html', {'error': '手机号未注册,请先注册!'})
    send_phone_code(phone)
    return render(request, 'user/code_login.html', {'phone': phone})


def message_board(request):
    if request.method == 'GET':
        if request.session.get('uid'):
            data = What.objects.all()
            return render(request, 'board.html', {'data': data})
        else:
            request.session['login_from'] = 'http://longlove.wang/board/'
            return render(request, 'user/login.html')

