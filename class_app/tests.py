from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CoursesModel, StudentClassModel

class CoursesAPITestCase(APITestCase):
    def setUp(self):
        # < ---- Creating initial data for testing ---- >
        CoursesModel.objects.create(name="Javascript")
        CoursesModel.objects.create(name="Python")

    def test_get_courses(self):
        # < ---- Test to receive the list of courses ---- >
        url = reverse('courses-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Javascript')
        self.assertEqual(response.data[1]['name'], 'Python')

    def test_create_course(self):
        # < ---- Test create a new course ---- >
        url = reverse('courses-list-create')
        data = {'name': 'History'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CoursesModel.objects.count(), 3)
        self.assertEqual(CoursesModel.objects.get(id=response.data['id']).name, 'History')


class CoursesAPITestCase(APITestCase):
    def setUp(self):

        # < ---- Create primary data for testing ---- >
        self.course1 = CoursesModel.objects.create(name="Math", teacher="Mr. Smith")
        self.course2 = CoursesModel.objects.create(name="Science", teacher="Dr. Brown")
        self.student = StudentClassModel.objects.create(name="John", family="Doe", age=25)
        self.student.courses.add(self.course1, self.course2)

    def test_get_courses(self):

        # < ---- Test to receive the list of courses ---- >
        url = reverse('courses-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Math')
        self.assertEqual(response.data[0]['teacher'], 'Mr. Smith')
        self.assertEqual(response.data[1]['name'], 'Science')
        self.assertEqual(response.data[1]['teacher'], 'Dr. Brown')

    def test_create_course(self):

        # < ---- Test create a new course ---- >
        url = reverse('courses-list-create')
        data = {'name': 'History', 'teacher': 'Prof. Lee'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CoursesModel.objects.count(), 3)
        self.assertEqual(CoursesModel.objects.get(id=response.data['id']).name, 'History')
        self.assertEqual(CoursesModel.objects.get(id=response.data['id']).teacher, 'Prof. Lee')

    def test_get_students(self):

        # < ---- Test to receive the list of students ---- >
        url = reverse('students-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John')
        self.assertEqual(response.data[0]['family'], 'Doe')
        self.assertEqual(response.data[0]['age'], 25)
        self.assertEqual(len(response.data[0]['courses']), 2)
        self.assertEqual(response.data[0]['courses'][0]['name'], 'Math')
        self.assertEqual(response.data[0]['courses'][0]['teacher'], 'Mr. Smith')
        self.assertEqual(response.data[0]['courses'][1]['name'], 'Science')
        self.assertEqual(response.data[0]['courses'][1]['teacher'], 'Dr. Brown')

    def test_create_student(self):

        # < ---- Test to create a new student ---- >
        url = reverse('students-list-create')
        data = {
            'name': 'Dayan',
            'family': 'Ghanbari',
            'age': 22,
            'courses': [{'id': self.course1.id, 'name': self.course1.name, 'teacher': self.course1.teacher},
                        {'id': self.course2.id, 'name': self.course2.name, 'teacher': self.course2.teacher}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StudentClassModel.objects.count(), 2)
        self.assertEqual(StudentClassModel.objects.get(id=response.data['id']).name, 'Dayan')
        self.assertEqual(StudentClassModel.objects.get(id=response.data['id']).family, 'Ghanbari')
        self.assertEqual(StudentClassModel.objects.get(id=response.data['id']).age, 22)
        self.assertEqual(len(StudentClassModel.objects.get(id=response.data['id']).courses.all()), 2)
