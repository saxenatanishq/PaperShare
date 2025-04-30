from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    DESIGNATION_CHOICES = [
        ('student', 'Student'),
        ('professor', 'Professor'),
    ]
    designation = models.CharField(max_length=10, choices=DESIGNATION_CHOICES,default='student')

class Paper(models.Model):
    name = models.CharField(max_length=100, default="subject")
    professor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="PapersOfProf")
    questions = models.CharField(max_length=200, default="[]")
    pdf_file = models.FileField(upload_to='checked_papers/')
    sections = models.ManyToManyField('Section', related_name="papers_of_section")
    open = models.BooleanField(default=True)

class Query(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="QueriesOfStudent")
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="QueriesOfPaper")
    identity = models.CharField(max_length=20)
    query = models.TextField()
    response = models.TextField(default="")
    change_of_marks = models.DecimalField(default=0, decimal_places=2,max_digits=10)
    resolved = models.BooleanField(default=False)

class Section(models.Model):
    name = models.CharField(max_length=100, default="")
    students = models.ManyToManyField(User,related_name="my_section")

class Answers(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="answers_of_paper")
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name="answers_of_students")
    pdf = models.FileField(upload_to='checked_papers/')