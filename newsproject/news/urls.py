from django.urls import path
from news.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login
# from news.views import index, get_category, view_news, add_news, test

urlpatterns = [
    # path('', index, name='Home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('news/add_news', add_news, name='add_news'),
    # path('test/', test, name='test')
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news', AddNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login')
]

