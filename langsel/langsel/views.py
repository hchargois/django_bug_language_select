from django.utils.translation import get_language
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', context={'cur_lang': get_language()})
