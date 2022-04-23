from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class BookListView(ListView):
    
    model = models.Book


class BookDetailView(DetailView):
    context_object_name = 'book_details'
    model = models.Book
    template_name = 'basic_app/book_detail.html'


class BookCreateView(CreateView):
    fields = ("name","author","location")
    model = models.Book


class BookUpdateView(UpdateView):
    fields = ("name","author")
    model = models.Book

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy("basic_app:list")
