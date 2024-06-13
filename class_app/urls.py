from django.urls import path
from .views import CoursesListCreateAPIView

urlpatterns = [
    # <--- Url Courses --->
    path('courses/', CoursesListCreateAPIView.as_view(), name='courses-list-create'),

]
