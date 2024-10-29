from django.contrib import admin
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path("publishers/<int:pk>/",views.publisher_edit,name="publisher_edit"),
    path("publishers/new/",views.publisher_edit, name="publisher_create"),
    path("book-search/",views.book_search, name="book_search"),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path("publishers/<int:pk>/",views.publisher_edit,name="publisher_edit"),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path(
        'api/all_books/',
        api_views.AllBooks.as_view(),
        name='all_books'
    ),

]