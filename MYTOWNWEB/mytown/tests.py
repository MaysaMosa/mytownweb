from django.test import TestCase
from .models import AddReport

class AddReportModelTest(TestCase):
    def setUp(self):
        AddReport.objects.create(
            title='Test Report',
            email='test@example.com',
            city='BEER',
            description='Test description',
            location='Test location'
        )

    def test_report_str_method(self):
        report = AddReport.objects.get(title='Test Report')
        self.assertEqual(str(report), 'Test Report')

    def test_report_save_and_retrieve(self):
       
        AddReport.objects.create(
            title='New Report',
            email='new@example.com',
            city='ASD',
            description='New description',
            location='New location'
        )
        
        saved_report = AddReport.objects.get(title='New Report')

        self.assertEqual(saved_report.title, 'New Report')
        self.assertEqual(saved_report.email, 'new@example.com')
        self.assertEqual(saved_report.city, 'ASD')
        self.assertEqual(saved_report.description, 'New description')
        self.assertEqual(saved_report.location, 'New location')
 

#  -----------------------------------------3 AI UNITESTS (copilot microsoft)------------------------------------------------------------------
        # Assuming you have a test case class set up (e.g., using Django's TestCase)

from django.test import TestCase
from django.urls import reverse
from .models import AddReport  # Import your model
from .views import addreports  # Import your view function

class AddReportsTestCase(TestCase):
    def test_successful_report_creation(self):
        # Simulate a POST request with valid data
        response = self.client.post(reverse('account/addreports.html'), {
            'title': 'Test Report',
            'city': 'Test City',
            'description': 'Test description',
            'location': 'Test location',
            # Add other required fields as needed
        })
        # Check if the report was created successfully
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(addreports.objects.count(), 1)  # Verify report creation

    def test_unsuccessful_report_creation(self):
        # Simulate a POST request with invalid data (e.g., missing fields)
        response = self.client.post(reverse('addreports'), {})
        # Check if no report was created
        self.assertEqual(response.status_code, 200)  # Form should be re-rendered
        self.assertEqual(addreports.objects.count(), 0)  # No report created

    def test_render_form(self):
        # Simulate a GET request
        response = self.client.get(reverse('addreports'))
        # Check if the form template is rendered
        self.assertEqual(response.status_code, 200)  # Form should be rendered
        self.assertTemplateUsed(response, 'account/addreports.html')  # Verify template


