from django.db import models
from django.utils import timezone

# Teacher Model
class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="Last Name"
    )
    password = models.CharField(max_length=50)  # Consider using Django's built-in user model for better security.
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, default='1234567890')
    
    CHOOSE_ADDRESS = [ 
        ('ktm', 'Kathmandu'),
        ('lat', 'Lalitpur'),
        ('bat', 'Bhaktapur'),
    ]
    
    address = models.CharField(max_length=40, choices=CHOOSE_ADDRESS, default='ktm')

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 

# Student Model 
class Student(models.Model):
    first_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="First Name")
    last_name = models.CharField(
        max_length=100, null=True, blank=False, verbose_name="Last Name")
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    roll_no = models.IntegerField(default=1)
    age = models.IntegerField(default=18)
    teachers = models.ManyToManyField(Teacher, through='StudentFaculty', related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

# Subject Marks Model  
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    def __str__(self): 
        return f"{self.student.first_name} - {self.subject.name} - {self.marks}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'subject'], name='unique_student_subject')
        ]

# Student Faculty Model
class StudentFaculty(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_faculties')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_faculties')
    faculty_name = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    today_day = models.DateTimeField(auto_now_add=True)
    class_timing = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.faculty_name} - {self.student.first_name} with {self.teacher.first_name}"
