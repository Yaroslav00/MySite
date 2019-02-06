from django.shortcuts import render
from django.http import Http404
from apps.myapp.models import Picture
from random import random

def start_page(request):
    if request.method == 'GET':
        pictures_landscapes = Picture.objects.filter(category='Landscapes')[:6]
        pictures_portraits = Picture.objects.filter(category='Portraits')[:6]
        pictures_stillLives = Picture.objects.filter(category='StillLives')[:6]
        pictures_marineArt = Picture.objects.filter(category='MarineArt')[:6]
        context = {}
        visiting_dict = {'Landscapes': int(request.COOKIES.get('Landscapes',0)),
        'StillLives': int(request.COOKIES.get('StillLives',0)),
        'Portraits': int(request.COOKIES.get('Portraits',0)), 
        'MarineArt': int(request.COOKIES.get('MarineArt',0))}
        max = 0
        imax = 'Landscapes'
        for i in visiting_dict:
            if max < visiting_dict[i]:
                max = visiting_dict[i]
                imax = i
        recommandations = list(Picture.objects.filter(category=imax))
        recommandations = recommandations[:4]
        for i in range(len(recommandations)):
                recommandations[i].index = i
        context['recommandations'] = recommandations[1:]
        context['first_recommanded'] = recommandations[0]
        context['pictures_landscapes'] = pictures_landscapes
        context['pictures_portraits'] = pictures_portraits
        context['pictures_stillLives'] = pictures_stillLives
        context['pictures_marineArt'] = pictures_marineArt
        response = render(request, 'myapp/index.html', context)
        return response


def page_with_category(request):
    if request.method == 'GET':
        category_name = request.GET.get('name')
        print(category_name)
        context = {}
        cnt = int(request.COOKIES.get(category_name, 0))
        pictures = Picture.objects.filter(category=category_name)
        context['category_name'] = category_name
        context['pictures'] = pictures
        response = render(request, 'myapp/category.html', context )
        response.set_cookie(category_name, cnt+1) 
        return response



def log_in(request):
    return render(request, 'myapp/LogIn.html')
