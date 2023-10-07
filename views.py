from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse('главная страница')


def greet(request, name):
    context = {'name': name.capitalize()}
    return render(request, 'my_app/index.html', context)


def it_is_new_year(request):
    today_day = datetime.datetime.now().day
    today_month = datetime.datetime.now().month
    context = {'name': today_day == 31 and today_month == 12}
    return render(request, 'my_app/index.html', context)