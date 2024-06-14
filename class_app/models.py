from django.db import models


# <--- Tabel Database "CoursesModel"--->
class CoursesModel(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30, default='Undefined')

    def __str__(self):
        return self.name


# <--- Tabel Database "StudentClassModel" --->
class StudentClassModel(models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    age = models.IntegerField()
    courses = models.ManyToManyField(CoursesModel, related_name='students')

    def __str__(self):
        return f"{self.name} {self.family}"
