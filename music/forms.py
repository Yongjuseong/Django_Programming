from django.forms import inlineformset_factory  
from music.models import Category, Music
from django import forms

MusicInlineFormSet = inlineformset_factory(Category, Music,
    fields = ['image', 'artist', 'title', 'description'],
    extra = 2)

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
