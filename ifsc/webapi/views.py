from django.http import HttpResponse
from django.db.models import Q
from django.template import loader
from django.shortcuts import render
from .models import ifscsearch
import json

def index(request):
    #template=loader.get_template('webapi/index.html')
    return render(request, 'webapi/index.html')

def ifsc(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        ifsc = ifscsearch.objects.all().filter(Q(ifsc__icontains=query)).distinct()
    else:
        ifsc = []
    data = []
    for each in ifsc:
        try:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
        except KeyError:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))

def bank(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        ifsc = ifscsearch.objects.all().filter(Q(bank_name__icontains=query)).distinct()
    else:
        ifsc = []
    data = []
    for each in ifsc:
        try:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
        except KeyError:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))

def state(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        ifsc = ifscsearch.objects.all().filter(Q(state__icontains=query)).distinct()
    else:
        ifsc = []
    data = []
    for each in ifsc:
        try:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
        except KeyError:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))

def district(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        ifsc = ifscsearch.objects.all().filter(Q(district__icontains=query)).distinct()
    else:
        ifsc = []
    data = []
    for each in ifsc:
        try:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
        except KeyError:
            myarr = {'ifsc' : each.ifsc,'bank_id' : each.bank_id,'branch' : each.branch,'address' : each.address,'city' : each.city,'district' : each.district,'state' : each.state,'bank_name' : each.bank_name}
            data.insert(0, myarr)
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))
