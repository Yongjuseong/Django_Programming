from django.contrib import admin
from sugang.models import Subject,Student
class StudentInline(admin.StackedInline):
    model = Student
    extra = 2

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = (StudentInline,)
    list_display = ('id', 'name', 'description')


@admin.register(Student) # 데코레이터 함수를  받아 명령을 추가 / 다시 함수 형태로 반환
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'major')