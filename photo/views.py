from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

class AlbumLV(ListView): #앨범 리스트뷰 
    model = Album

class AlbumDV(DetailView): # 앨범 디테일 뷰
    model = Album

class PhotoDV(DetailView): # 포토 디테일뷰
    model = Photo

