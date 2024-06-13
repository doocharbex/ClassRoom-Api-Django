from django.db import models


class CoursesModel(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30, default='Undefined')

    def __str__(self):
        return self.name


