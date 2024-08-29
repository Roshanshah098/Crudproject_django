from django.db import models
from django.utils import timezone
# from django.db.models.signals import post_save
# from django.dispatch import receiver 
# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50) #unique = True # Adjusted max_length for email
    phone = models.IntegerField(default=1234567890)
    passby = models.CharField(max_length= 40, default= "section1") 
    
    CHOOSE_ADDRESS = [
        ('ktm', 'Kathmandu'),
        ('lat', 'Lalitpur'),
        ('bat', 'Bhaktapur'),
    ]
    
    address = models.CharField(max_length=40, choices=CHOOSE_ADDRESS, default='ktm')

    def __str__(self):
        return self.first_name 

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    student_rollno = models.IntegerField(default = 1)
    student_age  = models.IntegerField(default = 18) 
    passby = models.CharField(max_length= 40, default= "section1") 
    teachers = models.ManyToManyField(Teacher, through='StudentFaculty', related_name='students')
    

    def __str__(self):   
        return self.first_name 

# @receiver(post_save, sender = Student)   #sender is equal to model
# def call_student_api(sender, instance, **kwargs):
#     print("Student created")
#     print(instance.first_name, sender, kwargs) 

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    
class Subject_marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "studentmarks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    marks = models.IntegerField(default = 0) 
    
    def __str__(self): 
        return f'{self.student.first_name} + " " + {self.subject.subject_name} + " " + {self.marks}'
    
    class Meta: 
        unique_together = ['student', 'subject'] # unique together means that the combination of student


class StudentFaculty(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_faculties')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_faculties', default=1)  # Use an existing teacher ID as default
    faculty_name = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    today_day = models.DateTimeField(auto_now_add=True)
    class_timing = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.faculty_name} - {self.student.first_name} with {self.teacher.first_name}"
