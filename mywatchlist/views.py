from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def index(request):
    my_watch_lists = MyWatchList.objects.all()
    
    watched = MyWatchList.objects.filter(watched=True).count()
    unwatched = MyWatchList.objects.filter(watched=False).count()
    if watched >= unwatched:
        pesan = 'Selamat, kamu sudah banyak menonton!'
    else:
        pesan = 'Wah, kamu masih sedikit menonton!'
    
    context = {
        'my_watch_lists': my_watch_lists,
        'pesan': pesan,
        'name': 'Emir Shamsuddin Fadhlurrahman',
        'student_id': '2106632541',
    }
    
    return render(request, 'mywatchlist_index.html', context)

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