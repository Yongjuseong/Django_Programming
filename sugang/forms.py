from django.forms import inlineformset_factory  
from sugang.models import Subject,Student


StudentInlineFormSet = inlineformset_factory(Subject, Student,
    fields = ['title', 'major','number','grade'],
    extra = 2)

