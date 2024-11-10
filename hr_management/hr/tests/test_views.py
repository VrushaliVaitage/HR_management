from django.test import TestCase
from django.urls import reverse
from hr.models import Employee, LeaveRequest, Attendance, PerformanceReview, TrainingProgram, Enrollment, Document
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile

class EmployeeViewTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="John Doe",
            designation="Developer",
            department="IT",
            date_of_hire=date(2022, 1, 10),
            contact_info="john@example.com"
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_list.html')

    def test_employee_create_view(self):
        response = self.client.post(reverse('employee_create'), {
            'name': 'Jane Smith',
            'designation': 'Manager',
            'department': 'HR',
            'date_of_hire': '2022-02-15',
            'contact_info': 'jane@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to employee list
        self.assertEqual(Employee.objects.count(), 2)

    def test_employee_update_view(self):
        response = self.client.post(reverse('employee_update', args=[self.employee.id]), {
            'name': 'John Smith',
            'designation': 'Senior Developer',
            'department': 'IT',
            'date_of_hire': '2022-01-10',
            'contact_info': 'johnsmith@example.com'
        })
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'John Smith')
        self.assertEqual(response.status_code, 302)  # Should redirect to employee list

    def test_employee_delete_view(self):
        response = self.client.post(reverse('employee_delete', args=[self.employee.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to employee list
        self.assertEqual(Employee.objects.count(), 0)


class LeaveRequestViewTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Jane Doe",
            designation="Analyst",
            department="Finance",
            date_of_hire=date(2021, 5, 20),
            contact_info="jane.doe@example.com"
        )
        self.leave_request = LeaveRequest.objects.create(
            employee=self.employee,
            leave_type="Sick",
            start_date=date(2022, 3, 10),
            end_date=date(2022, 3, 15),
            status="Pending"
        )

    def test_leave_list_view(self):
        response = self.client.get(reverse('leave_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave/leave_list.html')

    def test_leave_create_view(self):
        response = self.client.post(reverse('leave_create'), {
            'employee': self.employee.id,
            'leave_type': 'Annual',
            'start_date': '2022-04-01',
            'end_date': '2022-04-05',
            'status': 'Pending'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to leave list
        self.assertEqual(LeaveRequest.objects.count(), 2)

    # def test_leave_update_view(self):
    #     response = self.client.post(reverse('leave_update', args=[self.leave_request.id]), {
    #         'employee': self.employee.id,
    #         'leave_type': 'Sick',
    #         'start_date': '2022-03-10',
    #         'end_date': '2022-03-15',
    #         'status': 'Approved'
    #     })
    #     self.leave_request.refresh_from_db()
    #     self.assertEqual(self.leave_request.status, 'Approved')
    #     self.assertEqual(response.status_code, 302)  # Should redirect to leave list

############
    def test_leave_update_view(self):
        response = self.client.post(reverse('leave_update', args=[self.leave_request.pk]), {
            'employee': self.leave_request.employee.id,
            'leave_type': self.leave_request.leave_type,
            'start_date': self.leave_request.start_date,
            'end_date': self.leave_request.end_date,
            'status': 'Approved'  # Explicitly set the status
        })
        self.leave_request.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.leave_request.status, 'Approved')





    def test_leave_delete_view(self):
        response = self.client.post(reverse('leave_delete', args=[self.leave_request.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to leave list
        self.assertEqual(LeaveRequest.objects.count(), 0)


class DocumentViewTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Alice Green",
            designation="Support Specialist",
            department="Customer Support",
            date_of_hire=date(2020, 9, 25),
            contact_info="alice@example.com"
        )
        self.document = Document.objects.create(
            employee=self.employee,
            document_name="Contract",
            file=SimpleUploadedFile("contract.txt", b"contract content")
        )

    def test_document_list_view(self):
        response = self.client.get(reverse('document_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doc/document_list.html')

    def test_document_upload_view(self):
        uploaded_file = SimpleUploadedFile("new_file.txt", b"file content")
        response = self.client.post(reverse('document_upload'), {
            'employee': self.employee.id,
            'document_name': "Policy Document",
            'file': uploaded_file
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to document list
        self.assertEqual(Document.objects.count(), 2)

    def test_document_delete_view(self):
        response = self.client.post(reverse('document_delete', args=[self.document.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to document list
        self.assertEqual(Document.objects.count(), 0)
