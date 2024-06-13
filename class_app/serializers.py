from rest_framework import serializers
from .models import CoursesModel


# <--- Select the desired field to display data from the database --->
class CoursesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = ['id', 'name']

