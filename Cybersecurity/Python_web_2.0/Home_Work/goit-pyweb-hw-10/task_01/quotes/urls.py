##quotes/urls.py
from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('tag/<str:tag_name>/', views.quote_list, name='quote_list_by_tag'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('scrape/', views.scrape_quotes, name='scrape'),
]
