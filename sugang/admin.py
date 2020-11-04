from django.contrib import admin
from sugang.models import Subject,Student
class StudentInline(admin.StackedInline):
    model = Student
    extra = 2

@admin.register(Subject) # admin에 Subject 테이블 등록
class SubjectAdmin(admin.ModelAdmin):
    inlines = (StudentInline,)
    list_display = ('id', 'name', 'professor','place','description')


@admin.register(Student) # admin에 Student 테이블 등록 데코레이터 함수를  받아 명령을 추가 / 다시 함수 형태로 반환
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'major','number','grade')

