from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_hire = models.DateField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Leave', 'On Leave')])

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    comments = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.employee.name} - {self.review_date}"

class TrainingProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Enrollment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name} - {self.training_program.name}"

class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.employee.name} - {self.document_name}"
