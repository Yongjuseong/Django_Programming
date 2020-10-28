from django.db import models
from django.urls import reverse

class Subject(models.Model): # 수강 과목 클래스 정의
    name = models.CharField('NAME', max_length=30) #과목명
    description = models.CharField('One Line Description', max_length=100, blank=True) # 과목설명

    class Meta:
        ordering = ('id','name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sugang:subject_detail', args=(self.id,))


class Student(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    number = models.CharField('NUMBER', max_length=50, blank=False)  # 학번
    major = models.CharField('MAJOR',max_length=50,blank=False) #전공

    class Meta:
        ordering = ('title','number','major')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sugang:student_detail', args=(self.id,))
