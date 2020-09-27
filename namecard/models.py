from django.db import models

# Create your models here.
class Namecard_TBL(models.Model):
    name=models.CharField('NAME',max_length=100,blank=False)
    tel = models.CharField('MOBILE',max_length=50,blank=False)
    company = models.CharField('COMPANY', max_length=50, blank=False)
    email = models.CharField('EMAIL', max_length=50, blank=False)
    group = models.CharField('GROUP', max_length=50, blank=False)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True) # 현재 날짜 갱신
    birth_dt = models.DateTimeField('BIRTH DATE', auto_now=False)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('group','name',)


