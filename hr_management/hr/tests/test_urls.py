from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hr.views import (
    employee_list, employee_create, employee_update, employee_delete,
    leave_list, leave_create, leave_update, leave_delete,
    attendance_list, attendance_create,
    performance_list, performance_create, performance_update, performance_delete,
    training_list, training_create,
    enrollment_list, enrollment_create,
    document_list, document_upload, document_delete,
)

class UrlsTestCase(SimpleTestCase):
    # Employee URLs
    def test_employee_list_url(self):
        url = reverse('employee_list')
        self.assertEqual(resolve(url).func, employee_list)

    def test_employee_create_url(self):
        url = reverse('employee_create')
        self.assertEqual(resolve(url).func, employee_create)

    def test_employee_update_url(self):
        url = reverse('employee_update', args=[1])
        self.assertEqual(resolve(url).func, employee_update)

    def test_employee_delete_url(self):
        url = reverse('employee_delete', args=[1])
        self.assertEqual(resolve(url).func, employee_delete)

    # Leave URLs
    def test_leave_list_url(self):
        url = reverse('leave_list')
        self.assertEqual(resolve(url).func, leave_list)

    def test_leave_create_url(self):
        url = reverse('leave_create')
        self.assertEqual(resolve(url).func, leave_create)

    def test_leave_update_url(self):
        url = reverse('leave_update', args=[1])
        self.assertEqual(resolve(url).func, leave_update)

    def test_leave_delete_url(self):
        url = reverse('leave_delete', args=[1])
        self.assertEqual(resolve(url).func, leave_delete)

    # Attendance URLs
    def test_attendance_list_url(self):
        url = reverse('attendance_list')
        self.assertEqual(resolve(url).func, attendance_list)

    def test_attendance_create_url(self):
        url = reverse('attendance_create')
        self.assertEqual(resolve(url).func, attendance_create)

    # Performance URLs
    def test_performance_list_url(self):
        url = reverse('performance_list')
        self.assertEqual(resolve(url).func, performance_list)

    def test_performance_create_url(self):
        url = reverse('performance_create')
        self.assertEqual(resolve(url).func, performance_create)

    def test_performance_update_url(self):
        url = reverse('performance_update', args=[1])
        self.assertEqual(resolve(url).func, performance_update)

    def test_performance_delete_url(self):
        url = reverse('performance_delete', args=[1])
        self.assertEqual(resolve(url).func, performance_delete)

    # Training URLs
    def test_training_list_url(self):
        url = reverse('training_list')
        self.assertEqual(resolve(url).func, training_list)

    def test_training_create_url(self):
        url = reverse('training_create')
        self.assertEqual(resolve(url).func, training_create)

    # Enrollment URLs
    def test_enrollment_list_url(self):
        url = reverse('enrollment_list')
        self.assertEqual(resolve(url).func, enrollment_list)

    def test_enrollment_create_url(self):
        url = reverse('enrollment_create')
        self.assertEqual(resolve(url).func, enrollment_create)

    # Document URLs
    def test_document_list_url(self):
        url = reverse('document_list')
        self.assertEqual(resolve(url).func, document_list)

    def test_document_upload_url(self):
        url = reverse('document_upload')
        self.assertEqual(resolve(url).func, document_upload)

    def test_document_delete_url(self):
        url = reverse('document_delete', args=[1])
        self.assertEqual(resolve(url).func, document_delete)
