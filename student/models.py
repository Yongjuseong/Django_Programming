from django.db import models

# Create your models here.
class Student_TBL(models.Model):
    name=models.CharField('NAME',max_length=100,blank=False)
    number = models.CharField('NUMBER',max_length=50,blank=False)
    email = models.CharField('EMAIL', max_length=50, blank=False)
    status = models.CharField('STATUS', max_length=50, blank=False)
    major = models.CharField('MAJOR', max_length=50, blank=False)
    address = models.CharField('ADDRESS', max_length=50, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name','major',)