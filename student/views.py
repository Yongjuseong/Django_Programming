from django.shortcuts import render
from django.views.generic import ListView,DetailView
from student.models import Student_TBL
from django.views.generic import FormView #추가 Search Form
from student.forms import PostSearchForm #Search를 위해 추가
from django.db.models import Q #Search를 위해 추가
from django.shortcuts import render #Search를 위해 추가
# Create your views here.
class StudentLV(ListView): # StudentList 클래스형 뷰 정의
    model = Student_TBL
    context_object_name='student_tbls' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 정의
class StudentDV(DetailView): # StudentDetail 클래스형 뷰 정의
    model = Student_TBL
#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'student/student_post_search.html'
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        #filter -> icontrains => 대소문자 구분 X
        post_list = Student_TBL.objects.filter(Q(name__icontains=searchWord)| Q(number__icontains=searchWord) | Q(email__icontains=searchWord)|  Q(status__icontains=searchWord) | Q(major__icontains=searchWord)| Q(address__icontains=searchWord)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)   # No Redirection

