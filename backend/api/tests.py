from django.test import TestCase, Client
from django.urls import reverse

class TeacherDashboardAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_teacher_dashboard(self):
        response = self.client.get(reverse('get_teacher_dashboard'))
        self.assertEqual(response.status_code, 200)

