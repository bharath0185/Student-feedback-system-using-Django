

# Create your models here.
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=120)
    usn = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.student_name

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.student.student_name}"
