from rest_framework import serializers
from .models import CoursesModel, StudentClassModel


# <--- Select the desired field to display data from the database Tabel 'CoursesModel'--->
class CoursesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = ['id', 'name', 'teacher']


# <--- Select the desired field to display data from the database Tabel 'StudentClassModel' --->
class StudentClassModelSerializer(serializers.ModelSerializer):
    courses = CoursesModelSerializer(many=True)

    class Meta:
        model = StudentClassModel
        fields = ['id', 'name', 'family', 'age', 'courses']

    def create(self, validated_data):
        courses_data = validated_data.pop('courses')
        student = StudentClassModel.objects.create(**validated_data)
        for course_data in courses_data:
            course, created = CoursesModel.objects.get_or_create(**course_data)
            student.courses.add(course)
        return student

    def update(self, instance, validated_data):
        courses_data = validated_data.pop('courses')
        instance.name = validated_data.get('name', instance.name)
        instance.family = validated_data.get('family', instance.family)
        instance.age = validated_data.get('age', instance.age)
        instance.save()

        instance.courses.clear()
        for course_data in courses_data:
            course, created = CoursesModel.objects.get_or_create(**course_data)
            instance.courses.add(course)

        return instance
