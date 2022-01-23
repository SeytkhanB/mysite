
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


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

"""
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News List',
    }
    return render(request, template_name='news/index.html', context=context)
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

def view_news(request, news_id):

    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)     # gives to us page 'page not found'

    return render(request, 'news/view_news.html', {'news_item': news_item})

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


