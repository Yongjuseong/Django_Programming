from django.db import models
from django.urls import reverse
class Subject(models.Model): # 수강 과목 테이블 정의
    name = models.CharField('NAME', max_length=30) #과목명
    professor = models.CharField('PROFESSOR', max_length=30)  # 교수이름
    place = models.CharField('PLACE', max_length=30) #강의실
    description = models.CharField('One Line Description', max_length=100, blank=True) # 과목설명
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True,
                              null=True)  # edit위해 추가
    class Meta:
        ordering = ('id','name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('sugang:subject_detail', args=(self.id,))

class Student(models.Model): # 학생 테이블 정의
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) #수강 과목 외래키
    title = models.CharField('TITLE', max_length=30) # 이름
    number = models.CharField('NUMBER', max_length=50, blank=False)  # 학번
    major = models.CharField('MAJOR',max_length=50,blank=False) #전공
    grade = models.CharField('GRADE', max_length=50, blank=True,null=True)  # 학년
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True,
                              null=True)  # contents edit위해 추가
    class Meta:
        ordering = ('title','number','major')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sugang:student_detail', args=(self.id,))

