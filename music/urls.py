from django.urls import path
from music import views
app_name = 'music'
urlpatterns = [
    # Example: /music/
    path('', views.CategoryLV.as_view(), name='index'),

    # Example: /music/category/, same as /music/
    path('category', views.CategoryLV.as_view(), name='category_list'),

    # Example: /music/category/99/
    path('category/<int:pk>/', views.CategoryDV.as_view(), name='category_detail'),

    # Example: /music/music/99/
    path('music/<int:pk>/', views.MusicDV.as_view(), name='music_detail'),

    # Example: /music/category/add/
    path('category/add/', views.CategoryMusicCV.as_view(), name='category_add'),

    # Example: /music/category/change/
    path('category/change/', views.CategoryChangeLV.as_view(), name='category_change'),

    # Example: /music/category/99/update/
    path('category/<int:pk>/update/', views.CategoryMusicUV.as_view(), name='category_update'),

    # Example: /music/category/99/delete/
    path('category/<int:pk>/delete/', views.CategoryDelV.as_view(), name='category_delete'),

    # Example: /music/music/add/
    path('music/add/', views.MusicCV.as_view(), name='music_add'),

    # Example: /music/music/change/
    path('music/change/', views.MusicChangeLV.as_view(), name='music_change'),

    # Example: /music/music/99/update/
    path('music/<int:pk>/update/', views.MusicUV.as_view(), name='music_update'),

    # Example: /music/music/99/delete/
    path('music/<int:pk>/delete/', views.MusicDelV.as_view(), name='music_delete'),

    # Example: /category/search/
    path('category/search/',views.CategorySearchFormView.as_view(),name='category_search'),

    # Example: /music/search/
    path('music/search/',views.MusicSearchFormView.as_view(),name='music_search'),

]
