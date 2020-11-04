from django.contrib import admin
from photo.models import Album, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2

@admin.register(Album)  #앨범 모델 등록
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')


@admin.register(Photo) # 포토 모델 등록/ 데코레이터 함수를  받아 명령을 추가 / 다시 함수 형태로 반환
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')


