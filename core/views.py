from django.shortcuts import render
from pyshorteners import Shortener

from .models import Links

def home(request):
    hash_url = None
    short = None
    exists = None
    if request.method == 'POST':
        link = request.POST['link']

        s = Shortener()
        hash_url = s.tinyurl.short(link)

        exists = Links.objects.filter(short_link=hash_url).exists()
        if exists:
            short = hash_url
            hash_url = None

        if not exists:
            Links.objects.create(original_link=link, short_link=hash_url)

    context = {
        'hash_url': hash_url,
        'exists': exists, 
        'short': short,
    }

    return render(request, 'home.html', context)
