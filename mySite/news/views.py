
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# This is controller functions

def forTest(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/forTest.html', {'page_obj': page_obj})



# Changing controller functions to controller CLASSES below ↓
class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world this is mixin'
    # extra_context = {'title': 'Main'}
    paginate_by = 2

    # if we don't use method get_queryset(self): which is below then
    # here we should use queryset like ↓
    # queryset = News.objects.select_related('category')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = self.get_upper('main page')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')

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
class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    # if we don't use method get_queryset(self): which is below then
    # here we should use queryset like ↓
    # queryset = News.objects.select_related('category')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

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
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')        # I don't know why this line is here

    # login_url = '/admin/'                     # we will go to the admin
    # login_url = reverse_lazy('home')          # we will go to the home page
    raise_exception = True                      # we will go to the 403 page

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

