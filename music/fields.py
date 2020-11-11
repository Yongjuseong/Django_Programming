import os
from PIL import Image
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
class ThumbnailImageFieldFile(ImageFieldFile): #커스텀 필드 정의

    def _add_thumb(self, s):
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in ('jpeg', 'jpg'):
            parts[-1] = 'jpg'
        return '.'.join(parts)

    @property # 메소드를 멤버 변수처럼 사용가능 thumb_path 속성 생성
    def thumb_path(self):
        return self._add_thumb(self.path)

    @property  #  썸네일 url인 thumb_url 속성을 만듬
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True): #이미지 저장
        super().save(name, content, save)

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2))
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True): 
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField): #사용자 지정필드
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)

