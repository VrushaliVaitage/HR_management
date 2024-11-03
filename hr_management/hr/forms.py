from django import forms
from .models import Employee, LeaveRequest, Attendance, PerformanceReview, TrainingProgram, Enrollment, Document

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_hire', 'contact_info']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'status']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_date', 'comments', 'rating']

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = ['name', 'description', 'start_date', 'end_date']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['employee', 'training_program']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['employee', 'document_name', 'file']
