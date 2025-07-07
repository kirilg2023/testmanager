from django.shortcuts import render, get_object_or_404
from .models import Finder

def game_home(request):
    games=Finder.objects.order_by('title')
    return render(request,  'find_game/game_home.html',{'games':games})


def game_detail(request, post_slug):
    game = get_object_or_404(Finder, slug=post_slug)
    return render(request, 'find_game/details_view.html', {'finder': game})
