from django.views.generic import ListView, DetailView
from music.models import Category, Music
# contents edit 위해 추가한 import 부분 하단(below)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from music.forms import MusicInlineFormSet
from blog.models import Post
from django.views.generic import FormView #추가 Search Form
from music.forms import PostSearchForm #Search를 위해 추가
from django.db.models import Q #Search를 위해 추가
from django.shortcuts import render #Search를 위해 추가
from django.conf import settings

class CategoryLV(ListView): #카테고리 리스트뷰
    model = Category

class CategoryDV(DetailView): # 카테고리 디테일 뷰
    model = Category

class MusicDV(DetailView): # 음악 디테일뷰
    model = Music


#--- Create/Change-list/Update/Delete for Music edit 기능 추가
class MusicCV(LoginRequiredMixin, CreateView):
    model = Music
    fields = ('category', 'artist','title', 'image', 'description')
    success_url = reverse_lazy('music:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MusicChangeLV(LoginRequiredMixin, ListView):
    model = Music
    template_name = 'music/music_change_list.html'

    def get_queryset(self):
        return Music.objects.filter(owner=self.request.user)


class MusicUV(OwnerOnlyMixin, UpdateView):
    model = Music
    fields = ('category', 'artist','title', 'image', 'description')
    success_url = reverse_lazy('music:index')


class MusicDelV(OwnerOnlyMixin, DeleteView):
    model = Music
    success_url = reverse_lazy('music:index')


#--- Change-list/Delete for Category
class CategoryChangeLV(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'music/category_change_list.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryDelV(OwnerOnlyMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('music:index')


#--- (InlineFormSet) Create/Update for Category
class CategoryMusicCV(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('name', 'feeling','description')
    success_url = reverse_lazy('music:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MusicInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = MusicInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for musicform in formset:
            musicform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CategoryMusicUV(OwnerOnlyMixin, UpdateView):
    model = Category
    fields = ('name', 'feeling','description')
    success_url = reverse_lazy('music:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MusicInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = MusicInlineFormSet(instance=self.object)
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

#--- FormView
class CategorySearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'music/category_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        #filter -> icontrains => 대소문자 구분 X
        category_list = Category.objects.filter(Q(name__icontains=searchWord) |  Q(description__icontains=searchWord) | Q(feeling__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = category_list

        return render(self.request, self.template_name, context)   # No Redirection

#--- FormView
class MusicSearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'music/music_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        #filter -> icontrains => 대소문자 구분 X
        music_list = Music.objects.filter(Q(title__icontains=searchWord) |  Q(description__icontains=searchWord) | Q(artist__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = music_list

        return render(self.request, self.template_name, context)   # No Redirection