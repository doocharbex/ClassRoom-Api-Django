from django.urls import path
from .views import CoursesListCreateAPIView, StudentClassListCreateAPIView, StudentClassDetailAPIView


urlpatterns = [
    # <--- Url Courses --->
    path('courses/', CoursesListCreateAPIView.as_view(), name='courses-list-create'),

    # <--- Urls Students --->
    path('students/', StudentClassListCreateAPIView.as_view(), name='students-list-create'),
    path('students/<int:pk>/', StudentClassDetailAPIView.as_view(), name='student-detail'),

]
