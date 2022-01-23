
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm
from django.urls import reverse_lazy


# Changing controller functions to controller CLASSES below ↓
class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Main'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

# This is controller functions
"""
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News List',
    }
    return render(request, template_name='news/index.html', context=context)
"""

# Changing controller functions to CONTROLLER CLASSES below ↓
class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

# This is controller functions
"""
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)      # gives to us page 'page not found'

    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name='news/category.html', context=context)
"""

# Changing controller functions to CONTROLLER CLASSES below ↓
class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'                  # this line is using by default
    # template_name = 'news/news_detail.html'   # this line is using by default
    context_object_name = 'news_item'

# This is controller functions
"""
def view_news(request, news_id):

    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)     # gives to us page 'page not found'

    return render(request, 'news/view_news.html', {'news_item': news_item})
"""


# Changing controller functions to CONTROLLER CLASSES below ↓
class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')        # I don't know why this line is here

# This is controller functions
"""
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)        # ** means unpacking dictionaries
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm
    return render(request, 'news/add_news.html', {'form': form})
"""

