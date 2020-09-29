from django.shortcuts import render
from django.views.generic import ListView,DetailView
from namecard.models import Namecard_TBL

# Create your views here.
class NamecardLV(ListView): # NamecardList 클래스형 뷰 정의
    model = Namecard_TBL
    context_object_name='namecard_tbls' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 정의 

class NamecardDV(DetailView): # NamecardDetail 클래스형 뷰 정의
    model = Namecard_TBL
