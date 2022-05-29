from django.shortcuts import render
from main import Table_sorting
# Create your views here.
def get_menu_context():
    return [
        {'url_name': 'index'},
        {'url_name': 'time', 'name': 'Добавить данные', 'name1': 'Просмотр карты'},
    ]

def index_page(request):
    context = {
        'menu': get_menu_context(),
    }
    return render(request, 'pages/index.html', context)

def add_page(request):
    context = {
        'menu': get_menu_context(),
    }
    return render(request, 'pages/add.page.html', context)

def map_page(request):
    context = {
        'dic': Table_sorting.dic,
        'menu': get_menu_context(),
    }
    return render(request, 'pages/map.html', context)
