from django.shortcuts import render, redirect
# get_object_or_404
from .forms import NewsForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    return render(request, 'news/login.html')


class HomeNews(ListView, MyMixin):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(published=True).select_related('category')


class NewsByCategory(ListView, MyMixin):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'


# def test(request):
#     objects = ['jon', 'pol', 'george', 'jec', 'jon2', 'pol2', 'george2', 'jec2']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'News/test.html', {'page_obj': page_objects})


# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     content = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'News/index.html', context=content)
#
#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'News/category.html', context=context)
#
#
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item
#     }
#     return render(request, 'News/view_news.html', context=context)
#
#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.created(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': NewsForm})
