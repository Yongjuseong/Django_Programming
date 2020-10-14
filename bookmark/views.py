from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import FormView #추가 Search Form
from bookmark.forms import PostSearchForm #Search를 위해 추가
from django.db.models import Q #Search를 위해 추가
from django.shortcuts import render #Search를 위해 추가

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
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