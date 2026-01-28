from django.db import models

# Create your models here.


class Admission(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('AIML', 'CSE ( AI & ML )'),
        ('DS', 'CSE ( Data Science )'),
        ('MECH', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('EEE', 'Electrical Engineering'),
    ]

    parent_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.student_name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name