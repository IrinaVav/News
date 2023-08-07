from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


class AuthorList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model  =Author
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Имя шаблона, в котором будет показано, как пользователю должны выводиться объекты
    template_name = 'Authors.html'
    # Имя списка, в котором будут лежать все объекты
    context_object_name = 'authors'

# Create your views here.
