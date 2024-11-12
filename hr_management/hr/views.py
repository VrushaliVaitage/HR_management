from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, LeaveRequest, Attendance, PerformanceReview, TrainingProgram, Enrollment, Document
from .forms import EmployeeForm, LeaveRequestForm, AttendanceForm, PerformanceReviewForm, TrainingProgramForm, EnrollmentForm, DocumentForm
from django.contrib.auth.decorators import login_required

# Employee Management
@login_required(login_url='signin_url')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

@login_required(login_url='signin_url')
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required(login_url='signin_url')
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required(login_url='signin_url')
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})


# Leave Management Views
@login_required(login_url='signin_url')

def leave_list(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'leave/leave_list.html', {'leaves': leaves})

def leave_create(request):
    form = LeaveRequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('leave_list')
    return render(request, 'leave/leave_form.html', {'form': form})


def leave_update(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    form = LeaveRequestForm(request.POST or None, instance=leave)
    if form.is_valid():
        form.save()
        return redirect('leave_list')
    return render(request, 'leave/leave_form.html', {'form': form})

def leave_delete(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request, 'leave/leave_confirm_delete.html', {'leave': leave})

# Attendance Tracking Views
@login_required(login_url='signin_url')
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def attendance_create(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'attendance/attendance_form.html', {'form': form})

# Performance Reviews Views
@login_required(login_url='signin_url')
def performance_list(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'performance/performance_list.html', {'reviews': reviews})

def performance_create(request):
    form = PerformanceReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('performance_list')
    return render(request, 'performance/performance_form.html', {'form': form})

def performance_update(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    form = PerformanceReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('performance_list')
    return render(request, 'performance/performance_form.html', {'form': form})

def performance_delete(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('performance_list')
    return render(request, 'performance/performance_confirm_delete.html', {'review': review})

# Training Program Views
@login_required(login_url='signin_url')
def training_list(request):
    programs = TrainingProgram.objects.all()
    return render(request, 'enroll/training_list.html', {'programs': programs})

def training_create(request):
    form = TrainingProgramForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('training_list')
    return render(request, 'enroll/training_form.html', {'form': form})

# Enrollment Views (for assigning training programs to employees)
@login_required(login_url='signin_url')
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enroll/enrollment_list.html', {'enrollments': enrollments})

def enrollment_create(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('enrollment_list')
    return render(request, 'enroll/enrollment_form.html', {'form': form})

# Document Management Views
@login_required(login_url='signin_url')
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'doc/document_list.html', {'documents': documents})

def document_upload(request):
    form = DocumentForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('document_list')
    return render(request, 'doc/document_form.html', {'form': form})

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'doc/document_confirm_delete.html', {'document': document})
