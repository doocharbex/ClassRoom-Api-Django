from rest_framework import generics
from .models import CoursesModel
from .serializers import CoursesModelSerializer


# <---View Data Courses --->
class CoursesListCreateAPIView(generics.ListCreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesModelSerializer

