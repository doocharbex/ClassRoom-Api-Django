from rest_framework import generics
from .models import CoursesModel, StudentClassModel
from .serializers import CoursesModelSerializer, StudentClassModelSerializer


# <---View Data Courses --->
class CoursesListCreateAPIView(generics.ListCreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesModelSerializer


# <---View Data Student ClassList Create --->
class StudentClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentClassModel.objects.all()
    serializer_class = StudentClassModelSerializer


# <---View Data Selected Student Class Detail --->
class StudentClassDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentClassModel.objects.all()
    serializer_class = StudentClassModelSerializer