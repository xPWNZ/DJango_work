from django.http import HttpResponse
from django.shortcuts import render


def index(request): #Ссылка на HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request): #Ссылка на HttpRequest
    return HttpResponse("<h1>Статья по категориям</h1>")