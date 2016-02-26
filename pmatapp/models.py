# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Itemneigh(models.Model):
    mid = models.IntegerField(primary_key=True)
    list = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemneigh'


class Itemtopic(models.Model):
    mid = models.ForeignKey('Movie', db_column='mid', blank=True, null=True)
    tid = models.ForeignKey('Topic', db_column='tid', blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemtopic'


class Movie(models.Model):
    rate_ave = models.FloatField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    rate_cnt = models.IntegerField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    mid = models.IntegerField(primary_key=True)
    poster = models.CharField(max_length=100, blank=True, null=True)
    crew = models.TextField(blank=True, null=True)
    releasedate = models.DateField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    studio = models.TextField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    homepage = models.CharField(max_length=80, blank=True, null=True)
    trailer = models.CharField(max_length=80, blank=True, null=True)
    tids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class Plink(models.Model):
    mid = models.ForeignKey('Movie', db_column='mid', blank=True, null=True)
    pid = models.ForeignKey('Profile', db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plink'

class Profile(models.Model):
    pid = models.AutoField(primary_key=True)
    val = models.TextField(blank=True, null=True)
    dim = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'

class Topic(models.Model):
    tid = models.IntegerField(primary_key=True)
    eff_num_words = models.FloatField(blank=True, null=True)
    rank_1_docs = models.FloatField(blank=True, null=True)
    coherence = models.FloatField(blank=True, null=True)
    uniform_dist = models.FloatField(blank=True, null=True)
    tokens = models.FloatField(blank=True, null=True)
    document_entropy = models.FloatField(blank=True, null=True)
    corpus_dist = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic'

class MovieCate(models.Model):
    mid = models.IntegerField()
    dim = models.TextField(blank=True, null=True)
    pids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_cate'

class ItemtopicCut(models.Model):
    mid = models.ForeignKey('Movie', db_column='mid', blank=True, null=True)
    tid = models.ForeignKey('Topic', db_column='tid', blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemtopic_cut'

class Itempos(models.Model):
    mid = models.IntegerField(primary_key=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itempos'

class Topicdist(models.Model):
    tid1 = models.IntegerField(blank=True, null=True)
    tid2 = models.IntegerField(blank=True, null=True)
    dist = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topicdist'
