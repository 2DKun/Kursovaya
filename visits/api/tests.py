from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class StudentsTests(APITestCase):
    def test_vis_correct(self):
        url = reverse('students', args=['SELECT * FROM students'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": 'SELECT * FROM students',
            "res": "[(127, 'Mark', 'Volkov', 'Gymovich', 'IKBO-33-20', 'male'),"
                      " (201, 'Dany', 'Li', 'Каzyevich', 'INBO-08-20', 'female'),"
                      " (333, 'Billy', 'Herrington', 'NULL', 'IKBO-01-20', 'male'),"
                      " (921, 'Van', 'Tyomniy', 'Holmovich', 'INBO-01-20', 'male')]"
        })
    def test_vis_error(self):
        url = reverse('students', args=['921'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": '921',
            "res": 'near "921": syntax error'
        })

    def test_ept_error(self):
        url = reverse('students', args=[' '])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": ' ',
            "res": "[]"
        })

    def test_table_error(self):
        url = reverse('students', args=['SELECT * FROM student'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": 'SELECT * FROM student',
            "res": 'no such table: student'
        })

    def test_column_error(self):
        url = reverse('students', args=['SELECT class FROM students'])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "req": 'SELECT class FROM students',
            "res": 'no such column: class'
        })
