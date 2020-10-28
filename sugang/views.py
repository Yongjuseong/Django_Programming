from django.views.generic import ListView, DetailView
from sugang.models import Subject, Student

class SubjectLV(ListView): # 수강과목 리스트뷰
    model = Subject

class SubjectDV(DetailView): # 수강과목 디테일 뷰
    model = Subject

class StudentDV(DetailView): #학생 상세 정보
    model =Student
