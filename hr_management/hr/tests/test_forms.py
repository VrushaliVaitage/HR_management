from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from hr.forms import (
    EmployeeForm, LeaveRequestForm, AttendanceForm, PerformanceReviewForm,
    TrainingProgramForm, EnrollmentForm, DocumentForm
)
from hr. models import Employee, TrainingProgram


class EmployeeFormTest(TestCase):
    def test_employee_form_valid_data(self):
        form = EmployeeForm(data={
            'name': 'John Doe',
            'designation': 'Software Engineer',
            'department': 'IT',
            'date_of_hire': date(2022, 1, 15),
            'contact_info': 'johndoe@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_employee_form_missing_data(self):
        form = EmployeeForm(data={
            'name': '',
            'designation': 'Software Engineer',
            'department': 'IT',
            'date_of_hire': date(2022, 1, 15),
            'contact_info': 'johndoe@example.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)


class LeaveRequestFormTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Jane Smith",
            designation="Project Manager",
            department="Operations",
            date_of_hire=date(2021, 5, 10),
            contact_info="janesmith@example.com"
        )

    def test_leave_request_form_valid_data(self):
        form = LeaveRequestForm(data={
            'employee': self.employee.id,
            'leave_type': 'Annual',
            'start_date': date(2023, 11, 1),
            'end_date': date(2023, 11, 5)
        })
        self.assertTrue(form.is_valid())

    def test_leave_request_form_invalid_dates(self):
        form = LeaveRequestForm(data={
            'employee': self.employee.id,
            'leave_type': 'Annual',
            'start_date': date(2023, 11, 5),
            'end_date': date(2023, 11, 1)  # End date is before start date
        })
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)


class AttendanceFormTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Mark Taylor",
            designation="HR Specialist",
            department="HR",
            date_of_hire=date(2020, 2, 20),
            contact_info="marktaylor@example.com"
        )

    def test_attendance_form_valid_data(self):
        form = AttendanceForm(data={
            'employee': self.employee.id,
            'date': date(2024, 11, 1),
            'status': 'Present'
        })
        self.assertTrue(form.is_valid())

    def test_attendance_form_invalid_status(self):
        form = AttendanceForm(data={
            'employee': self.employee.id,
            'date': date(2024, 11, 1),
            'status': 'Unknown'  # Invalid choice
        })
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)


class PerformanceReviewFormTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Lucy Hale",
            designation="Data Scientist",
            department="Analytics",
            date_of_hire=date(2023, 3, 1),
            contact_info="lucyhale@example.com"
        )

    def test_performance_review_form_valid_data(self):
        form = PerformanceReviewForm(data={
            'employee': self.employee.id,
            'review_date': date(2024, 3, 1),
            'comments': "Excellent performance",
            'rating': 5
        })
        self.assertTrue(form.is_valid())

    def test_performance_review_form_invalid_rating(self):
        form = PerformanceReviewForm(data={
            'employee': self.employee.id,
            'review_date': date(2024, 3, 1),
            'comments': "Excellent performance",
            'rating': 6  # Rating should be within allowed range, e.g., 1-5
        })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)


class TrainingProgramFormTest(TestCase):
    def test_training_program_form_valid_data(self):
        form = TrainingProgramForm(data={
            'name': "Django Fundamentals",
            'description': "An introductory course to Django",
            'start_date': date(2024, 2, 1),
            'end_date': date(2024, 2, 28)
        })
        self.assertTrue(form.is_valid())

    def test_training_program_form_invalid_dates(self):
        form = TrainingProgramForm(data={
            'name': "Django Fundamentals",
            'description': "An introductory course to Django",
            'start_date': date(2024, 2, 28),
            'end_date': date(2024, 2, 1)  # End date is before start date
        })
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)


class EnrollmentFormTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Emily Clark",
            designation="Product Designer",
            department="Design",
            date_of_hire=date(2022, 8, 1),
            contact_info="emilyclark@example.com"
        )
        self.training_program = TrainingProgram.objects.create(
            name="Advanced Python",
            description="Deep dive into Python programming",
            start_date=date(2024, 4, 1),
            end_date=date(2024, 4, 30)
        )

    def test_enrollment_form_valid_data(self):
        form = EnrollmentForm(data={
            'employee': self.employee.id,
            'training_program': self.training_program.id
        })
        self.assertTrue(form.is_valid())


class DocumentFormTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Tom Green",
            designation="IT Support",
            department="Support",
            date_of_hire=date(2021, 6, 1),
            contact_info="tomgreen@example.com"
        )

    def test_document_form_valid_data(self):
        uploaded_file = SimpleUploadedFile("file.txt", b"file_content")
        form = DocumentForm(data={
            'employee': self.employee.id,
            'document_name': "Resume"
        }, files={'file': uploaded_file})
        self.assertTrue(form.is_valid())

    def test_document_form_missing_file(self):
        form = DocumentForm(data={
            'employee': self.employee.id,
            'document_name': "Resume"
        })  # Missing file
        self.assertFalse(form.is_valid())
        self.assertIn('file', form.errors)
