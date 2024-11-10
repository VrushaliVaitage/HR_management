from django.test import TestCase
from hr.models import Employee, LeaveRequest, Attendance, PerformanceReview, TrainingProgram, Enrollment, Document
from datetime import date

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="John Doe",
            designation="Software Engineer",
            department="IT",
            date_of_hire=date(2022, 1, 15),
            contact_info="johndoe@example.com"
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "John Doe")
        self.assertEqual(self.employee.designation, "Software Engineer")
        self.assertEqual(self.employee.department, "IT")
        self.assertEqual(self.employee.date_of_hire, date(2022, 1, 15))
        self.assertEqual(self.employee.contact_info, "johndoe@example.com")

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "John Doe")


class LeaveRequestModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Jane Smith",
            designation="Project Manager",
            department="Operations",
            date_of_hire=date(2021, 5, 10),
            contact_info="janesmith@example.com"
        )
        self.leave_request = LeaveRequest.objects.create(
            employee=self.employee,
            leave_type="Annual",
            start_date=date(2023, 11, 1),
            end_date=date(2023, 11, 5),
            status="Pending"
        )

    def test_leave_request_creation(self):
        self.assertEqual(self.leave_request.employee, self.employee)
        self.assertEqual(self.leave_request.leave_type, "Annual")
        self.assertEqual(self.leave_request.start_date, date(2023, 11, 1))
        self.assertEqual(self.leave_request.end_date, date(2023, 11, 5))
        self.assertEqual(self.leave_request.status, "Pending")

    def test_leave_request_str(self):
        self.assertEqual(str(self.leave_request), "Jane Smith - Annual")


class AttendanceModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Mark Taylor",
            designation="HR Specialist",
            department="HR",
            date_of_hire=date(2020, 2, 20),
            contact_info="marktaylor@example.com"
        )
        self.attendance = Attendance.objects.create(
            employee=self.employee,
            date=date(2024, 11, 1),
            status="Present"
        )

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.employee, self.employee)
        self.assertEqual(self.attendance.date, date(2024, 11, 1))
        self.assertEqual(self.attendance.status, "Present")

    def test_attendance_str(self):
        self.assertEqual(str(self.attendance), "Mark Taylor - 2024-11-01 - Present")


class PerformanceReviewModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Lucy Hale",
            designation="Data Scientist",
            department="Analytics",
            date_of_hire=date(2023, 3, 1),
            contact_info="lucyhale@example.com"
        )
        self.performance_review = PerformanceReview.objects.create(
            employee=self.employee,
            review_date=date(2024, 3, 1),
            comments="Excellent performance",
            rating=5
        )

    def test_performance_review_creation(self):
        self.assertEqual(self.performance_review.employee, self.employee)
        self.assertEqual(self.performance_review.review_date, date(2024, 3, 1))
        self.assertEqual(self.performance_review.comments, "Excellent performance")
        self.assertEqual(self.performance_review.rating, 5)

    def test_performance_review_str(self):
        self.assertEqual(str(self.performance_review), "Lucy Hale - 2024-03-01")


class TrainingProgramModelTest(TestCase):
    def setUp(self):
        self.training_program = TrainingProgram.objects.create(
            name="Django Fundamentals",
            description="An introductory course to Django",
            start_date=date(2024, 2, 1),
            end_date=date(2024, 2, 28)
        )

    def test_training_program_creation(self):
        self.assertEqual(self.training_program.name, "Django Fundamentals")
        self.assertEqual(self.training_program.description, "An introductory course to Django")
        self.assertEqual(self.training_program.start_date, date(2024, 2, 1))
        self.assertEqual(self.training_program.end_date, date(2024, 2, 28))





class EnrollmentModelTest(TestCase):
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
        self.enrollment = Enrollment.objects.create(
            employee=self.employee,
            training_program=self.training_program
        )

    def test_enrollment_creation(self):
        self.assertEqual(self.enrollment.employee, self.employee)
        self.assertEqual(self.enrollment.training_program, self.training_program)

    def test_enrollment_str(self):
        self.assertEqual(str(self.enrollment), "Emily Clark - Advanced Python")


class DocumentModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Tom Green",
            designation="IT Support",
            department="Support",
            date_of_hire=date(2021, 6, 1),
            contact_info="tomgreen@example.com"
        )
        self.document = Document.objects.create(
            employee=self.employee,
            document_name="Resume",
            file="documents/resume.pdf"
        )

    def test_document_creation(self):
        self.assertEqual(self.document.employee, self.employee)
        self.assertEqual(self.document.document_name, "Resume")
        self.assertEqual(self.document.file, "documents/resume.pdf")

    def test_document_str(self):
        self.assertEqual(str(self.document), "Tom Green - Resume")