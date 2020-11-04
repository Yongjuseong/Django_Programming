from django.views.generic import ListView, DetailView
from sugang.models import Subject, Student
#edit 위해 추가
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from sugang.forms import StudentInlineFormSet

class SubjectLV(ListView): # 수강과목 리스트뷰
    model = Subject

class SubjectDV(DetailView): # 수강과목 디테일 뷰
    model = Subject

class StudentDV(DetailView): #학생 상세 정보
    model =Student


#--- Create/Change-list/Update/Delete for Student edit 기능 추가
class StudentCV(LoginRequiredMixin, CreateView):
    model = Student
    fields = ('subject','title', 'number', 'grade', 'major')
    success_url = reverse_lazy('sugang:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StudentChangeLV(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'sugang/Student_change_list.html'

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)


class StudentUV(OwnerOnlyMixin, UpdateView):
    model = Student
    fields = ('subject','title', 'number', 'grade', 'major')
    success_url = reverse_lazy('sugang:index')


class StudentDelV(OwnerOnlyMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('sugang:index')


#--- Change-list/Delete for subject
class SubjectChangeLV(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'sugang/subject_change_list.html'

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)


class SubjectDelV(OwnerOnlyMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('sugang:index')


#--- (InlineFormSet) Create/Update for subject
class SubjectStudentCV(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('name', 'professor','place','description')
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = StudentInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = StudentInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for studentform in formset:
            studentform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SubjectStudentUV(OwnerOnlyMixin, UpdateView):
    model = Subject
    fields = ('name', 'professor','place','description')
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = StudentInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = StudentInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))