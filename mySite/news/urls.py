

from django.urls import path
from .views import HomeNews, NewsByCategory, ViewNews, CreateNews

urlpatterns = [
    # path('test/', forTest, name='fotTest'),
    path('test/', HomeNews.as_view(), name='forTest'),

    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),

    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'SOMETHING'}), name='category'),

    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),

    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]



# DON'T FORGET TO ADD as_view
