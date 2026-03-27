from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STUDENT = 'student'
    REGISTRAR = 'registrar'
    LECTURER = 'lecturer'
    HOD = 'hod'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (REGISTRAR, 'Academic Registrar'),
        (LECTURER, 'Lecturer'),
        (HOD, 'Head of Department'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    student_number = models.CharField(max_length=20, blank=True)  # students only
    department = models.CharField(max_length=100, blank=True)     # staff only

    def is_student(self):
        return self.role == self.STUDENT

    def is_registrar(self):
        return self.role == self.REGISTRAR