from django.shortcuts import render
from .models import RoutePartial
from .models import MainRouteV1
from .models import RouteVersion1
from .models import SailPartial
from .models import PortVersion1
import json
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
from django.core import serializers

# Create your views here.


def index(request):
    pass
    return render(request, 'pre/index.html')


def research(request):
    pass
    return render(request, 'pre/research.html')


def search(request):
    shiproute = []
    if request.method == "POST":
        d = request.POST
        q = SailPartial.objects.none()
        ship = SailPartial.objects.filter(imo=d['IMO'], departuretime__range=(d['SD'], d['ED']))
        for i in ship:
            x = i.routeid
            p = RoutePartial.objects.filter(routeid=x)
            q = q | p
        # j = json.dumps(list(q), default=lambda obj: obj.__dict__)
        # shiproute = eval(j)
        # print(q)
        port = PortVersion1.objects.all().values()
        pj = json.dumps(list(port), default=lambda obj: obj.__dict__)
        portdict = eval(pj)

    return render(request, 'pre/search.html', {'shiproute': q, 'portdict': portdict})


def result(request):
    p = MainRouteV1.objects.filter(sea_flag=1).values()
    # p = RoutePartial.objects.all().values()
    j = json.dumps(list(p), default=lambda obj: obj.__dict__)
    dict = eval(j)
    port = PortVersion1.objects.all().values()
    pj = json.dumps(list(port), default=lambda obj: obj.__dict__)
    portdict = eval(pj)
    # print(dict)
    return render(request, 'pre/result.html', {'dict': dict, 'portdict': portdict})
    # return HttpResponse(names)
    # return render_to_response("pre/result.html", locals())
