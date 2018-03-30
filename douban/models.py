from django.db import models


class MovieInfo(models.Model):
    # 电影名称
    movieName = models.CharField(max_length=100)
    # 电影id
    movieId = models.IntegerField()
    # 海报
    img = models.CharField(max_length=100)
    # 电影信息网址
    info_website = models.CharField(max_length=100)
    # 评分
    data_score = models.CharField(max_length=30)
    # 片长
    data_duration = models.CharField(max_length=100)
    # 上映日期
    data_release = models.CharField(max_length=100)
    # 导演
    data_director = models.CharField(max_length=100)
    # 主演
    data_actors = models.CharField(max_length=100)
    # 制作国家
    data_region = models.CharField(max_length=100)
    # 编剧
    data_attrs = models.CharField(max_length=150)
    # 评论人数
    data_number = models.IntegerField()
    # 简介
    introduction = models.TextField()
    # 类型
    movie_type = models.CharField(max_length=100)
    # 语言
    movie_language = models.CharField(max_length=100)
    # 又名
    also_called = models.CharField(max_length=150)
    # 排名
    movie_ranking = models.CharField(max_length=100)
    # 短评地址
    comment_website = models.CharField(max_length=100)

    class Meta:
        db_table = 'movie_info'


class MovieComment(models.Model):
    # 网友名称
    netName = models.CharField(max_length=50)
    # 电影id
    movieId = models.IntegerField()
    # 电影名称
    movieName = models.CharField(max_length=100)
    # 星级
    states = models.CharField(max_length=20)
    # 短评内容
    content = models.TextField()
    # 评论时间
    contentTime = models.CharField(max_length=100)
    # 短评网址
    comment_website = models.CharField(max_length=100)
    # 头像
    netImg = models.CharField(max_length=100)

    class Meta:
        db_table = 'movie_comment'

    @classmethod
    def create_comment(cls, netName, movieId, movieName, states, content, contentTime, comment_website, netImg):
        u = cls(netName=netName, movieId=movieId, movieName=movieName, states=states, content=content,
                contentTime=contentTime, comment_website=comment_website, netImg=netImg)
        return u


class MovieHome(models.Model):
    # 电影id
    movieId = models.IntegerField()
    # 电影名称
    movieName = models.CharField(max_length=100)
    # 好评
    praise_rate = models.CharField(max_length=10)
    # 一般
    general_rate = models.CharField(max_length=10)
    # 差评
    negative_rate = models.CharField(max_length=10)
    # 短评地址
    comment_website = models.CharField(max_length=100)
    # 海报
    img = models.CharField(max_length=100)
    # 电影信息网址
    info_website = models.CharField(max_length=100)

    class Meta:
        db_table = 'movie_home'


class BookInfo(models.Model):
    # 书名
    book_name = models.CharField(max_length=100)
    # 书籍id
    book_id = models.IntegerField()
    # 封面
    img = models.CharField(max_length=100)
    # 作者
    book_author = models.CharField(max_length=100)
    # 出版社
    book_press = models.CharField(max_length=100)
    # 出品方
    book_party = models.CharField(max_length=100)
    # 原作者
    book_original_name = models.CharField(max_length=100)
    # 译者
    book_translator = models.CharField(max_length=100)
    # 出版年
    book_publication = models.CharField(max_length=100)
    # 页数
    book_number = models.CharField(max_length=100)
    # 定价
    book_price = models.CharField(max_length=100)
    # 装帧
    book_binding = models.CharField(max_length=100)
    # 丛书
    book_series = models.CharField(max_length=100)
    # 评分
    book_score = models.CharField(max_length=100)
    # 书籍信息地址
    book_info_website = models.CharField(max_length=100)
    # 短评地址
    book_comment_website = models.CharField(max_length=100)
    # 评论人数
    data_number = models.CharField(max_length=100)
    # 简介
    introduction = models.TextField()

    class Meta:
        db_table = 'book_info'


class BookComment(models.Model):
    # 网友名称
    net_name = models.CharField(max_length=100)
    # 书籍id
    book_id = models.IntegerField()
    # 书名
    book_name = models.CharField(max_length=100)
    # 星级
    states = models.CharField(max_length=100)
    # 短评内容
    content = models.TextField()
    # 评论时间
    contentTime = models.CharField(max_length=100)
    # 短评地址
    book_comment_website = models.CharField(max_length=100)
    # 头像
    net_img = models.CharField(max_length=100)

    class Meta:
        db_table = 'book_comment'

    @classmethod
    def create_comment(cls, net_name, book_id, book_name, states, content, contentTime, book_comment_website, net_img):
        u = cls(net_name=net_name, book_id=book_id, book_name=book_name, states=states, content=content,
                contentTime=contentTime, book_comment_website=book_comment_website, net_img=net_img)
        return u


class BookHome(models.Model):
    # 书籍id
    book_id = models.IntegerField()
    # 书籍名称
    book_name = models.CharField(max_length=100)
    # 书籍短评地址
    book_comment_website = models.CharField(max_length=100)
    # 封面
    img = models.CharField(max_length=100)
    # 书籍信息地址
    book_info_website = models.CharField(max_length=100)

    class Meta:
        db_table = 'book_home'


class MusicInfo(models.Model):
    # 专辑名称
    music_name = models.CharField(max_length=100)
    # 专辑id
    music_id = models.IntegerField()
    # 封面
    img = models.CharField(max_length=100)
    # 表演者
    music_performer = models.CharField(max_length=100)
    # 流派
    music_schools = models.CharField(max_length=100)
    # 类型
    music_type = models.CharField(max_length=100)
    # 介质
    music_medium = models.CharField(max_length=100)
    # 发行时间
    music_release = models.CharField(max_length=100)
    # 出版者
    music_publisher = models.CharField(max_length=100)
    # 唱片数
    music_number = models.CharField(max_length=100)
    # 条形码
    music_code = models.CharField(max_length=100)
    # 其他版本
    music_Other = models.CharField(max_length=100)
    # ISRC(中国)
    music_ISRC = models.CharField(max_length=100)
    # 评分
    music_score = models.CharField(max_length=100)
    # 信息网址
    music_info_website = models.CharField(max_length=100)
    # 短评地址
    music_comment_website = models.CharField(max_length=100)
    # 评论人数
    data_number = models.CharField(max_length=100)
    # 简介
    introduction = models.TextField()
    # 曲目
    song = models.TextField()

    class Meta:
        db_table = 'music_info'


class MusicComment(models.Model):
    # 网友名称
    net_name = models.CharField(max_length=100)
    # 专辑id
    music_id = models.IntegerField()
    # 专辑名称
    music_name = models.CharField(max_length=100)
    # 星级
    states = models.CharField(max_length=100)
    # 短评
    content = models.TextField()
    # 评论时间
    contentTime = models.CharField(max_length=100)
    # 短评地址
    music_comment_website = models.CharField(max_length=100)
    # 头像
    net_img = models.CharField(max_length=100)

    class Meta:
        db_table = 'music_comment'

    @classmethod
    def create_comment(cls, net_name, music_id, music_name, states, content, contentTime, music_comment_website, net_img):
        u = cls(net_name=net_name, music_id=music_id, music_name=music_name, states=states, content=content,
                contentTime=contentTime, music_comment_website=music_comment_website, net_img=net_img)
        return u


class MusicHome(models.Model):
    # 专辑id
    music_id = models.IntegerField()
    # 专辑名称
    music_name = models.CharField(max_length=100)
    # 短评网址
    music_comment_website = models.CharField(max_length=100)
    # 封面
    img = models.CharField(max_length=100)
    # 信息网址
    music_info_website = models.CharField(max_length=100)

    class Meta:
        db_table = 'music_home'


class User(models.Model):
    # 手机号
    phone = models.CharField(max_length=11)
    # 网名
    net_name = models.CharField(max_length=50)
    # 网友头像
    net_img = models.ImageField()
    # 性别
    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )
    sex = models.CharField(max_length=8, choices=SEX)
    # 年龄
    age = models.IntegerField()
    # 密码
    password = models.CharField(max_length=16)
    # token
    # user_token = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    @classmethod
    def create_comment(cls, phone, net_name, password, net_img, sex, age):
        u = cls(phone=phone, net_name=net_name, password=password, net_img=net_img, sex=sex, age=age)
        return u


class What(models.Model):
    # 网名
    net_name = models.CharField(max_length=50)
    # 手机号
    phone = models.CharField(max_length=11)
    # 内容
    content = models.TextField()

    class Meta:
        db_table = 'what'

    @classmethod
    def create_comment(cls, net_name, phone, content):
        u = cls(net_name=net_name, phone=phone, content=content)
        return u
