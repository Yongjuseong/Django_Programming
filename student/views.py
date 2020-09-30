from django.shortcuts import render
from django.views.generic import ListView,DetailView
from student.models import Student_TBL

# Create your views here.
class StudentLV(ListView): # StudentList 클래스형 뷰 정의
    model = Student_TBL
    context_object_name='student_tbls' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 정의

class StudentDV(DetailView): # StudentDetail 클래스형 뷰 정의
    model = Student_TBL
