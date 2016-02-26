from django.shortcuts import render
from pmatapp import models
from django.http import HttpResponse
from django.db.models import Q
from collections import *
import json
# Create your views here.
# for new user
cate = ['genres', 'keyword', 'crew', 'cast', 'studio']
def register(request):
    return render(request, 'trailindex.html')

# change start point, change topic
def get_new_setting(request):

    # the focus item is changed, change neighbor
    # coordinates stay same
    mid = int(request.GET['mid'])
    request.session['mid'] = mid
    request.session['neighbor'] = json.loads(models.Itemneigh.objects.get(mid=mid).list)

    tid = int(request.GET['tid'])
    if tid >=0:
        request.session['tid'] = tid
    else:
        request.session['tid'] = models.ItemtopicCut.objects.filter(mid=mid).order_by('-weight')[0].tid

    return HttpResponse('success', content_type='text')

# input: mid
# put into visited list
# a template to show movie detail
def get_details(request):
    m = models.Movie.objects.filter(mid=request.GET['mid'])[0]
    request.session['visited'].append(request.GET['mid'])
    return render(request, 'detail.html', {
        'title': m.title,
        'poster': m.poster
    })

def get_snap(request):
    m = models.Movie.objects.filter(mid=request.GET['mid'])[0]
    return render(request, 'snap.html',
                  {
                      'title': m.title,
                      'poster':m.poster,
                      'rate': m.rate_ave
                  })

def clean_visit_list(request):
    request.session['visited'] =[]
    return HttpResponse('success', content_type='text')

# no input
# update focus item and neighbor
# return: tid list
def get_topic_list(request):
    return HttpResponse(json.dumps([{'tid': t.tid_id, 'weight': t.weight}
                       for t in models.ItemtopicCut.objects.filter(mid=request.session['mid']).order_by('-weight')]))
    # return HttpResponse(models.Movie.objects.filter(mid=request.session['mid'])[0].tids)

# input tid
def getlist(request):
    tid = request.GET['tid']
    res = []
    neigh = request.session['neighbor']
    for i in models.ItemtopicCut.objects.filter(tid=tid).order_by('-weight'):
        mid = str(i.mid_id)
        res.append({
            'mid': i.mid_id,
            'weight': i.weight,
            'order': neigh[mid][0] if mid in neigh and int(tid) in neigh[mid][1] else 0
        })

    return HttpResponse(json.dumps(res))

def get_overview(request):
    return HttpResponse(json.dumps([{'mid': i.mid,
                                 'x': i.x,
                                 'y': i.y
                                 } for i in models.Itempos.objects.all()]))