from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def index(request):
#     topics=Topic.objects.all()
#     webpages=Webpage.objects.all()
#     authors=AccessRecord.objects.all()
#     return render(request, 'index.html', {'topics': topics,'webpages':webpages, 'authors': authors})

def insert_topic(request):
    topic_name=input('Enter Topic Name:')
    to=Topic.objects.get_or_create(topic_name=topic_name)
    if to[1]:
        LTO=Topic.objects.all()
        d={'LTO': LTO}
        return render(request, 'index.html', d)
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
            LWO=Webpage.objects.all()
            d={'LWO': LWO}
            return render(request, 'web.html',d)
        else:
            return HttpResponse(f'Webpage {url} is already exist.')
    else:
        return HttpResponse(f'You entered topic name {topic_name} is not exist in parent table.')

def insert_accessrecord(request):
    PK=int(input('Enter PK value'))
    WTO=Webpage.objects.filter(pk=PK)
    if WTO:
        AR=WTO[0]
        author=input('Enter Author Name:')
        date=input('Enter Date in (YYYY-MM-DD):')
        price=float(input('Enter Price:'))
        ARTO=AccessRecord.objects.get_or_create(name=AR,author=author, date=date, price=price)
        if ARTO[1]:
            LAO=AccessRecord.objects.all()
            d={'LAO': LAO}
            return render(request, 'access.html',d)
        else:
            return HttpResponse('Access Record is already exists.')
    else:
        return HttpResponse('You entered webpage  is not exist in parent table.')
