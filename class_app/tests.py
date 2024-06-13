from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CoursesModel

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
