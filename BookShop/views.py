from django.shortcuts import render


# Create your views here.

def welcome_view(request):
    content = {
        "greetings": "Добро пожаловать в наш интернет-магазин!"
    }
    return render(request, 'BookShop/base.html', context=content)
