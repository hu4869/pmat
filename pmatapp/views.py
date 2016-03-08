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

    tid = int(request.GET['tid'])
    if tid >=0:
        request.session['tid'] = tid
    else:
        request.session['tid'] = models.ItemtopicCut.objects.filter(mid=mid).order_by('-weight')[0].tid

    return HttpResponse('success', content_type='text')

# input: mid, tid(for highlighting)
# a template to show movie detail
def get_details(request):
    mids = [t.mid_id for t in models.ItemtopicCut.objects.filter(tid=request.GET['tid'])]
    pids = models.Plink.objects.filter(mid__in=mids)
    m = models.Movie.objects.get(mid=request.GET['mid'])
    ps = models.Plink.objects.filter(mid=request.GET['mid'])
    dim = defaultdict(list)
    for p in ps:
        w = pids.filter(pid = p.pid).count()
        dim[p.pid.dim].append({'val':p.pid.val, 'w':w, 'pid': p.pid_id, 'tool': p.val})
    # request.session['visited'].append(request.GET['mid'])
    res = {}
    res['dims'] = [{'key':k, 'val':v} for k,v in dim.items()]
    res['title'] = m.title
    res['poster'] = m.poster
    res['overview'] = m.overview

    return render(request, 'detail.html', res)

def get_snap(request):
    m = models.Movie.objects.get(mid=request.GET['mid'])
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
    return HttpResponse(json.dumps([{'tid': t.tid, 'weight': t.weight}
                       for t in models.ItemtopicCut.objects.filter(mid=request.session['mid']).order_by('-weight')]))
    # return HttpResponse(models.Movie.objects.filter(mid=request.session['mid'])[0].tids)

# input tid
def getlist(request):
    tid = request.GET['tid']
    res = []
    neigh = json.loads(models.Itemneigh.objects.get(id=str(request.session['mid'])+'-'+tid).list)

    for i in models.ItemtopicCut.objects.filter(tid=tid).order_by('-weight'):
        mid = str(i.mid_id)
        res.append({
            'mid': i.mid_id,
            'weight': i.weight,
            'order': neigh[mid] if mid in neigh else 0
        })

    return HttpResponse(json.dumps(res))

def get_overview(request):
    return HttpResponse(json.dumps([{'mid': i.mid,
                                 'x': i.x,
                                 'y': i.y
                                 } for i in models.Itempos.objects.all()]))

def get_topic_snap(request):
    tid = request.GET['tid'];
    mids = []
    for m in models.ItemtopicCut.objects.filter(tid=tid).order_by('-weight')[:10]:
        mids.append({
            'title': m.mid.title,
            'mid': m.mid_id,
            'poster': m.mid.poster
        })
    pids = defaultdict(list)
    for p in models.Catetopic.objects.filter(tid=tid).order_by('-l_w'):
        if p.pid.count > 14:
            dim = p.pid.dim
            pids[p.pid.dim].append({
                'val': p.pid.val,
                'l_w': p.l_w,
                'g_w': p.g_w,
                'pid': p.pid_id
            })
    p = []
    for dim, pid in pids.items():
        p.append({'dim':dim, 'p':pid[:10]})
    return render(request, 'topic_snap.html', {'mid':mids,'pid':p})

def search(request):
    term = request.GET['term']
    res = []
    for p in models.Movie.objects.filter(title__contains=term).order_by('-popularity')[:5]:
        res.append({'id': p.mid, 'label': p.title, 'category':'m'})
    for p in models.Profile.objects.filter(val__contains=term).order_by('-count')[:5]:
        res.append({'id': p.pid, 'label': p.val,'category':'p'})

    return HttpResponse(json.dumps(res))

def biggest_topic(request):
    return HttpResponse(models.ItemtopicCut.objects.filter(mid=request.GET['mid']).order_by('-weight')[0].tid)
