from django import forms
from .models import Employee, LeaveRequest, Attendance, PerformanceReview, TrainingProgram, Enrollment, Document
from django.core.exceptions import ValidationError


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_hire', 'contact_info']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date']

        def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")
        
            if start_date and end_date and end_date < start_date:
                raise ValidationError("End date cannot be before start date.")

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_date', 'comments', 'rating']

        def clean_rating(self):
            rating = self.cleaned_data.get("rating")
            if not (1 <= rating <= 5):
                raise ValidationError("Rating must be between 1 and 5.")
            return rating

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = ['name', 'description', 'start_date', 'end_date']

        def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")

            if start_date and end_date and end_date < start_date:
                raise ValidationError("End date cannot be before start date.")

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['employee', 'training_program']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['employee', 'document_name', 'file']
