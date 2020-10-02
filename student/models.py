from django.db import models

# Create your models here.
class Student_TBL(models.Model):
    name=models.CharField('NAME',max_length=100,blank=False) #이름
    number = models.CharField('NUMBER',max_length=50,blank=False) # 학번
    email = models.CharField('EMAIL', max_length=50, blank=False) # Email 주소
    status = models.CharField('STATUS', max_length=50, blank=False) #학적 상태
    major = models.CharField('MAJOR', max_length=50, blank=False) #전공
    address = models.CharField('ADDRESS', max_length=50, blank=False) #주소
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name','major',)

