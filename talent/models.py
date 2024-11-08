from django.db import models
from django.contrib.auth.models import User


# Student model linked to a User
class Student(models.Model):
    user = models.OneToOneField(User, related_name="student_profile", on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    state_of_residence = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username  # Display the username as a representative name for each student


# Talent model linked to the Student model
class Talent(models.Model):
    student = models.ForeignKey(Student, related_name="talents", on_delete=models.CASCADE)
    talent_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional description for each talent

    def __str__(self):
        return f"{self.talent_name} - {self.student.user.username}"
