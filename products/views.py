from django.shortcuts import render

# Create your views here.
# Контроллеры = views(вьюхи) = функции


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


# Тестовый контроллер для пеердачи динамики
def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
        'products': [

        ],
    }
    return render(request, 'products/test-context.html', context)
