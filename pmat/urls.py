"""pmat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pmatapp import views as pmat

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', pmat.register),
    url(r'^set', pmat.get_new_setting),
    url(r'^detail', pmat.get_details),
    url(r'^snap', pmat.get_snap),
    url(r'^item_list', pmat.getlist),
    url(r'^clean_visit_list$', pmat.clean_visit_list),
    url(r'^topic_snap', pmat.get_topic_snap),
    url(r'^search', pmat.search),
    url(r'^get_biggest_topic', pmat.biggest_topic),

    url(r'^topic_list$', pmat.get_topic_list),
    url(r'^overview$', pmat.get_overview),
]
