from django.contrib import admin
from django.urls import path, include

from news.views import index, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
