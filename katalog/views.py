from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    catalog_items = CatalogItem.objects.all()
    context = {
        'catalog_items': catalog_items,
        'name': 'Emir Shamsuddin Fadhlurrahman',
        'student_id': '2106632541',
    }
    
    return render(request, 'katalog.html', context)
