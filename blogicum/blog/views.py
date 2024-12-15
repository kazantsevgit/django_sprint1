from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение...''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль...''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь...''',
    },
]

def index(request):
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, id):
    post = next((post for post in posts if post['id'] == id), None)
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category_slug': category_slug})
