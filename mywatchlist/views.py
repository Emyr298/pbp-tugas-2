from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_html(request):
    my_watch_lists = MyWatchList.objects.all()
    context = {
        'my_watch_lists': my_watch_lists
    }
    
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    my_watch_lists = MyWatchList.objects.all()
    
    return HttpResponse(serializers.serialize('xml', my_watch_lists), content_type='application/xml')

def show_json(request):
    my_watch_lists = MyWatchList.objects.all()
    
    return HttpResponse(serializers.serialize('json', my_watch_lists), content_type='application/json')