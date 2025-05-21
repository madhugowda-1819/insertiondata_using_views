from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    topics=Topic.objects.all()
    webpages=Webpage.objects.all()
    authors=AccessRecord.objects.all()
    return render(request, 'index.html', {'topics': topics,'webpages':webpages, 'authors': authors})

def insert_topic(request):
    topic_name=input('Enter Topic Name:')
    to=Topic.objects.get_or_create(topic_name=topic_name)
    if to[1]:
        return HttpResponse(f'Topic {topic_name} is created.')
    else:
        return HttpResponse(f'Topic {topic_name} is already exists.')
    

def insert_webpage(request):
    topic_name=input('Enter Topic Name:')
    LTO=Topic.objects.filter(topic_name=topic_name)
    if LTO:
        TO=LTO[0]
        name=input('Enter Name:')
        url=input('Enter URL:')
        email=input('Enter Email:')
        TTo=Webpage.objects.get_or_create(topic_name=TO, name=name, url=url,email=email)
        if TTo[1]:
            return HttpResponse(f'Webpage {url} is created.')
        else:
            return HttpResponse(f'Webpage {url} is already exist.')
    else:
        return HttpResponse(f'You entered topic name {topic_name} is not exist in parent table.')

def insert_accessrecord(request):
    Webpage_name=input('Enter webpage Name:')
    WTO=Webpage.objects.filter(name=Webpage_name)
    if WTO:
        AR=WTO[0]
        author=input('Enter Author Name:')
        date=input('Enter Date in (YYYY-MM-DD):')
        price=float(input('Enter Price:'))
        ARTO=AccessRecord.objects.get_or_create(name=AR,author=author, date=date, price=price)
        if ARTO[1]:
            return HttpResponse('Access Record is created.')
        else:
            return HttpResponse('Access Record is already exists.')
    else:
        return HttpResponse(f'You entered webpage name {Webpage_name} is not exist in parent table.')
