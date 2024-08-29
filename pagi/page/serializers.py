from rest_framework import serializers
from .models import Student, Teacher, Subject, SubjectMarks, StudentFaculty

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['id', 'first_name', 'last_name', 'image', 'roll_no', 'age', 'teachers']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'password', 'email', 'phone', 'address']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class SubjectMarksSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = SubjectMarks
        fields = ['id', 'student', 'subject', 'marks']

class StudentFacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFaculty
        fields = ['id', 'student', 'teacher', 'faculty_name', 'class_room', 'today_day', 'class_timing']

class CourseSerializer(serializers.Serializer):
    course = serializers.CharField(max_length=100)
    
    def validate_course(self, value):
        pass
        # Optional: Add custom validation for course_name here
        return value

class ClassAssignmentSerializer(serializers.Serializer):
    class_name = serializers.CharField(max_length=100)  
    class_room = serializers.CharField(max_length=100) 
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())  # Assuming student ID is passed
    
    def validate_class_name(self, value):
        # Optional: Add custom validation for class_name here
        pass
        return value

    def validate_class_room(self, value):
        # Optional: Add custom validation for class_room here
        pass
        return value
