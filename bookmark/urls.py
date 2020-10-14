from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),

    # Example: /bookmark/search/
    path('search/', views.SearchFormView.as_view(), name='search'),

]

