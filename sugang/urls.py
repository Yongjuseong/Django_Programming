from django.urls import path
from sugang import views

app_name = 'sugang'

urlpatterns = [
    # Example: /sugang/
    path('', views.SubjectLV.as_view(), name='index'),

    # Example: /sugang/subject, same as /sugang/
    path('subject', views.SubjectLV.as_view(), name='subject_list'),

    # Example: /sugang/album/99/
    path('subject/<int:pk>/', views.SubjectDV.as_view(),name='subject_detail'),

    # Example: /sugang/student
    path('student/<int:pk>/', views.StudentDV.as_view(), name='student_detail'),

]

'''
urlpatterns = [
    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # Example: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # Example: /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

]
'''