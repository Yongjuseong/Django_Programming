from django.contrib import admin
from music.models import Category, Music

class MusicInline(admin.StackedInline):
    model = Music
    extra = 2

@admin.register(Category)  #카테고리 모델 등록
class CategoryAdmin(admin.ModelAdmin):
    inlines = (MusicInline,)
    list_display = ('id', 'name', 'feeling','description')


@admin.register(Music) # 음악, 뮤직 모델 등록/ 데코레이터 함수를  받아 명령을 추가 / 다시 함수 형태로 반환
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'title','upload_dt')