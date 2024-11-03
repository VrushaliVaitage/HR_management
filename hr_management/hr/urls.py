
from django.urls import path
from .views import (
    employee_list, employee_create, employee_update, employee_delete,
    leave_list, leave_create, leave_update, leave_delete,
    attendance_list, attendance_create,
    performance_list, performance_create, performance_update, performance_delete,
    training_list, training_create,
    enrollment_list, enrollment_create,
    document_list, document_upload, document_delete,
)

urlpatterns = [
    # Employee URLs
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', employee_create, name='employee_create'),
    path('employees/edit/<int:pk>/', employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', employee_delete, name='employee_delete'),

    # Leave URLs
    path('leaves/', leave_list, name='leave_list'),
    path('leaves/add/', leave_create, name='leave_create'),
    path('leaves/edit/<int:pk>/', leave_update, name='leave_update'),
    path('leaves/delete/<int:pk>/', leave_delete, name='leave_delete'),

    # Attendance URLs
    path('attendance/', attendance_list, name='attendance_list'),
    path('attendance/add/', attendance_create, name='attendance_create'),

    # Performance URLs
    path('performance/', performance_list, name='performance_list'),
    path('performance/add/', performance_create, name='performance_create'),
    path('performance/edit/<int:pk>/', performance_update, name='performance_update'),
    path('performance/delete/<int:pk>/', performance_delete, name='performance_delete'),

    # Training URLs
    path('training/', training_list, name='training_list'),
    path('training/add/', training_create, name='training_create'),

    # Enrollment URLs
    path('enrollments/', enrollment_list, name='enrollment_list'),
    path('enrollments/add/', enrollment_create, name='enrollment_create'),

    # Document URLs
    path('documents/', document_list, name='document_list'),
    path('documents/upload/', document_upload, name='document_upload'),
    path('documents/delete/<int:pk>/', document_delete, name='document_delete'),
]
