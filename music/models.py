from django.db import models
from django.urls import reverse
from music.fields import ThumbnailImageField #직접만든 커스텀필드 정의
class Category(models.Model): #음악 카테고리(앨범) 테이블 정의
    name = models.CharField('NAME', max_length=30)
    feeling = models.CharField('FEELING',max_length=30) # 카테고리의 느낌
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True,null=True)  # contents edit위해 추가
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('music:category_detail', args=(self.id,))

class Music(models.Model): #음악 테이블 정의
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #음악의 카테고리
    title = models.CharField('TITLE', max_length=30)
    artist = models.CharField('ARTIST',max_length=30) # 가수 
    description = models.TextField('Music Description', blank=True)
    image = ThumbnailImageField('IMAGE', upload_to='music/%Y/%m')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True) #발매일
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True) # contents edit위해 추가
    class Meta:
        ordering = ('title',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('music:music_detail', args=(self.id,))


