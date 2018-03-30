# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_name', models.CharField(max_length=100)),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=100)),
                ('states', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('contentTime', models.CharField(max_length=100)),
                ('book_comment_website', models.CharField(max_length=100)),
                ('net_img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'book_comment',
            },
        ),
        migrations.CreateModel(
            name='BookHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=100)),
                ('book_comment_website', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('book_info_website', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'book_home',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_id', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_press', models.CharField(max_length=100)),
                ('book_party', models.CharField(max_length=100)),
                ('book_original_name', models.CharField(max_length=100)),
                ('book_translator', models.CharField(max_length=100)),
                ('book_publication', models.CharField(max_length=100)),
                ('book_number', models.CharField(max_length=100)),
                ('book_price', models.CharField(max_length=100)),
                ('book_binding', models.CharField(max_length=100)),
                ('book_series', models.CharField(max_length=100)),
                ('book_score', models.CharField(max_length=100)),
                ('book_info_website', models.CharField(max_length=100)),
                ('book_comment_website', models.CharField(max_length=100)),
                ('data_number', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
            ],
            options={
                'db_table': 'book_info',
            },
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netName', models.CharField(max_length=50)),
                ('movieId', models.IntegerField()),
                ('movieName', models.CharField(max_length=100)),
                ('states', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('contentTime', models.CharField(max_length=100)),
                ('comment_website', models.CharField(max_length=100)),
                ('netImg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'movie_comment',
            },
        ),
        migrations.CreateModel(
            name='MovieHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField()),
                ('movieName', models.CharField(max_length=100)),
                ('praise_rate', models.CharField(max_length=10)),
                ('general_rate', models.CharField(max_length=10)),
                ('negative_rate', models.CharField(max_length=10)),
                ('comment_website', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('info_website', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'movie_home',
            },
        ),
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=100)),
                ('movieId', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('info_website', models.CharField(max_length=100)),
                ('data_score', models.CharField(max_length=30)),
                ('data_duration', models.CharField(max_length=100)),
                ('data_release', models.CharField(max_length=100)),
                ('data_director', models.CharField(max_length=100)),
                ('data_actors', models.CharField(max_length=100)),
                ('data_region', models.CharField(max_length=100)),
                ('data_attrs', models.CharField(max_length=150)),
                ('data_number', models.IntegerField()),
                ('introduction', models.TextField()),
                ('movie_type', models.CharField(max_length=100)),
                ('movie_language', models.CharField(max_length=100)),
                ('also_called', models.CharField(max_length=150)),
                ('movie_ranking', models.CharField(max_length=100)),
                ('comment_website', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'movie_info',
            },
        ),
        migrations.CreateModel(
            name='MusicComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_name', models.CharField(max_length=100)),
                ('music_id', models.IntegerField()),
                ('music_name', models.CharField(max_length=100)),
                ('states', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('contentTime', models.CharField(max_length=100)),
                ('music_comment_website', models.CharField(max_length=100)),
                ('net_img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'music_comment',
            },
        ),
        migrations.CreateModel(
            name='MusicHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_id', models.IntegerField()),
                ('music_name', models.CharField(max_length=100)),
                ('music_comment_website', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('music_info_website', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'music_home',
            },
        ),
        migrations.CreateModel(
            name='MusicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=100)),
                ('music_id', models.IntegerField()),
                ('img', models.CharField(max_length=100)),
                ('music_performer', models.CharField(max_length=100)),
                ('music_schools', models.CharField(max_length=100)),
                ('music_type', models.CharField(max_length=100)),
                ('music_medium', models.CharField(max_length=100)),
                ('music_release', models.CharField(max_length=100)),
                ('music_publisher', models.CharField(max_length=100)),
                ('music_number', models.CharField(max_length=100)),
                ('music_code', models.CharField(max_length=100)),
                ('music_Other', models.CharField(max_length=100)),
                ('music_ISRC', models.CharField(max_length=100)),
                ('music_score', models.CharField(max_length=100)),
                ('music_info_website', models.CharField(max_length=100)),
                ('music_comment_website', models.CharField(max_length=100)),
                ('data_number', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('song', models.TextField()),
            ],
            options={
                'db_table': 'music_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('net_name', models.CharField(max_length=50)),
                ('net_img', models.ImageField(upload_to='')),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女'), ('U', '保密')], max_length=8)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='What',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'what',
            },
        ),
    ]