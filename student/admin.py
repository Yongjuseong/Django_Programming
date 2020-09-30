from django.contrib import admin
from student.models import Student_TBL

# Register your models here.
@admin.register(Student_TBL)
class Student_TBLAdmin(admin.ModelAdmin):
    list_display = ('id','name','number') # admin에서 보여주는 항목
