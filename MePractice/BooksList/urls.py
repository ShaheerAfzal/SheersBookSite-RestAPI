from django.urls import path, include

from . import views
from .models import bookReviews

urlpatterns = [
    path('<int:pk>/', views.BookDetailAPIview.as_view(), name='book-detail'),
    path('', views.BookListCreateAPIview.as_view(), name='book-list-create'),
    path('all/', views.BookListAPIview.as_view(), name='book-list'),
    #path('Reviews/<int:pk>/', views.ReviewDetailAPIview.as_view(), name='review-detail'), #shows details of a singular review
    path('Reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('Reviews/all/', views.ReviewListAPIview.as_view(), name='review-list'),
    path('Reviews/book/<int:book_id>/', views.BookReviewListAPIview.as_view(), name='book-review-list'),
    path('Reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'), # shows details and allows CRUD of a review
    path('Stores/', views.StoreListCreateAPIView.as_view(), name='store-list-create'),
    path('Stores/all/', views.StoreListAPIview.as_view(), name='store-list'),
    path('Stores/book/<int:book_id>/', views.BookStoreListAPIview.as_view(), name='book-store-list'),
    path('Stores/<int:pk>/', views.StoreRetrieveUpdateDestroyAPIView.as_view(), name='store-retrieve-update-destroy'),
]
