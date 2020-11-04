from django.urls import path
from sugang import views

app_name = 'sugang'

urlpatterns = [
    # Example: /sugang/
    path('', views.SubjectLV.as_view(), name='index'),

    # Example: /sugang/subject, same as /sugang/
    path('subject', views.SubjectLV.as_view(), name='subject_list'),

    # Example: /sugang/subject/99/
    path('subject/<int:pk>/', views.SubjectDV.as_view(),name='subject_detail'),

    # Example: /sugang/student
    path('student/<int:pk>/', views.StudentDV.as_view(), name='student_detail'),

    # Example: /sugang/subject/add/
    path('subject/add/', views.SubjectStudentCV.as_view(), name='subject_add'),

    # Example: /sugang/subject/change/
    path('subject/change/', views.SubjectChangeLV.as_view(), name='subject_change'),

    # Example: /sugang/subject/99/update/
    path('subject/<int:pk>/update/', views.SubjectStudentUV.as_view(), name='subject_update'),

    # Example: /sugang/subject/99/delete/
    path('subject/<int:pk>/delete/', views.SubjectDelV.as_view(), name='subject_delete'),

    # Example: /sugang/student/add/
    path('student/add/', views.StudentCV.as_view(), name='student_add'),

    # Example: /sugang/student/change/
    path('student/change/', views.StudentChangeLV.as_view(), name='student_change'),

    # Example: /sugang/studet/99/update/
    path('student/<int:pk>/update/', views.StudentUV.as_view(), name='student_update'),

    # Example: /sugang/student/99/delete/
    path('student/<int:pk>/delete/', views.StudentDelV.as_view(), name='student_delete'),
]
