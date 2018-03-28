from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('blogs/', include('blogs.urls')),
    path('comments/', include('comments.urls')),
    path('books/', include('books.urls')),
    path('movies/', include('movies.urls')),
    path('friends/', include('friends.urls')),
    path('admin/', admin.site.urls),
]
