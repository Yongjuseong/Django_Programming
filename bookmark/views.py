from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import FormView #추가 Search Form
from bookmark.forms import PostSearchForm #Search를 위해 추가
from django.db.models import Q #Search를 위해 추가
from django.shortcuts import render #Search를 위해 추가

from django.views.generic import CreateView, UpdateView, DeleteView #콘텐츠 편집기능 위해 추가
from django.contrib.auth.mixins import LoginRequiredMixin #콘텐츠 편집기능 위해 추가
from django.urls import reverse_lazy #콘텐츠 편집기능 위해 추가
from mysite.views import OwnerOnlyMixin #콘텐츠 편집기능 위해 추가

class BookmarkLV(ListView): # BookmarkList 클래스형 뷰 정의
    model = Bookmark
class BookmarkDV(DetailView): # BookmarkDetail 클래스형 뷰 정의
    model = Bookmark
#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'bookmark/bookmark_post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        #filter -> icontrains => 대소문자 구분 X
        post_list = Bookmark.objects.filter(Q(title__icontains=searchWord)|  Q(url__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)   # No Redirection


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')