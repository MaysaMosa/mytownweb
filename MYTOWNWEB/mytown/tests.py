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
 

#  -----------------------------------------3 AI UNITESTS------------------------------------------------------------------