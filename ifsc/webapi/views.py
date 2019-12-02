from django.http import HttpResponse
from django.db.models import Q
from django.template import loader
from .models import ifscsearch
import json

def index(request):
    return HttpResponse("Shekhar's API for Bank IFSC Search")

def search(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        ifsc = ifscsearch.objects.all().filter(Q(ifsc__icontains=query) |
                                            Q(bank_id__icontains=query) |
                                            Q(branch__icontains=query) |
                                            Q(address__icontains=query) |
                                            Q(city__icontains=query) |
                                            Q(district__icontains=query) |
                                            Q(state__icontains=query) |
                                            Q(bank_name__icontains=query)).distinct()
    else:
        ifsc = []
    data = {}
    for each in ifsc:
        try:
            data[each.id].append({'ifsc' : each.ifsc,
                                    'bank_id' : each.bank_id,
                                    'branch' : each.branch,
                                    'address' : each.address,
                                    'city' : each.city,
                                    'district' : each.district,       
                                    'state' : each.state,
                                    'bank_name' : each.bank_name})
        except KeyError:
            data[each.id].append({'ifsc' : each.ifsc,
                                    'bank_id' : each.bank_id,
                                    'branch' : each.branch,
                                    'address' : each.address,
                                    'city' : each.city,
                                    'district' : each.district,       
                                    'state' : each.state,
                                    'bank_name' : each.bank_name})
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))
