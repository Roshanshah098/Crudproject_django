# #  managers.py 
# from .models import Student, Teacher, Subject, SubjectMarks, StudentFaculty

# class StudentService:
    
#     @staticmethod
#     def add_course(student, course_name):   
#         # Logic to add a course to the student
#         course, created = Subject.objects.get_or_create(name=course_name) 
#         SubjectMarks.objects.create(student=student, subject=course, marks=0)
#         return course 

# class TeacherService:  
    
#     @staticmethod
#     def assign_class(teacher, class_name):
#         # Logic to assign a class to the teacher
#         StudentFaculty.objects.create(teacher=teacher, faculty_name=class_name)
#         return class_name
