# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
# #from rest_framework.pagination import PageNumberPagination
# #from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.pagination import CursorPagination 
# from .serializers import StudentSerializer, TeacherSerializer  
# from .models import Student 

# Define a custom pagination class if you want to customize the page_size
# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'pg'
#     page_size_query_param = 'records'
#     max_page_size = 6 
#     last_page_strings = 'end'
  
    
#/studentapi/?limit=5&offset=3 , offset where it starts from ; 
# limit is how many you want to see

# class MylimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     max_limit = 10
#     limit_query_param = 'rec'
#     offset_query_param = 'start' 
    
from rest_framework import viewsets, status
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer, ClassAssignmentSerializer
from .models import Student, Teacher, StudentFaculty

class MyCursorPagination(CursorPagination):  
    page_size = 5
    ordering = 'first_name'
    cursor_query_param = 'pg'
    page_size_query_param = 'records'
    max_page_size = 6 

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_course(self, request, pk=None):
        student = self.get_object()   
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():   
            course_name = serializer.validated_data['course']
            # You may want to handle the creation or lookup of the course here
            try:
                course = student.add_course(course_name) 
            except Exception as e: 
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': f'Course {course_name} added to student {student.first_name}.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False)
    def recent_students(self, request):
        """
        A custom action to get a list of recently added students.
        """
        recent_students = Student.objects.all().order_by('-id')

        page = self.paginate_queryset(recent_students)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_students, many=True)
        return Response(serializer.data)

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = MyCursorPagination
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post']) 
    def assign_class(self, request, pk=None):
        teacher = self.get_object()
        serializer = ClassAssignmentSerializer(data=request.data)

        if serializer.is_valid():
            class_name = serializer.validated_data['class_name']
            class_room = serializer.validated_data['class_room']
            student = serializer.validated_data.get('student')

            if student is None:
                return Response({'error': 'Student is required.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                teacher.assign_class(class_name)
                StudentFaculty.objects.create(
                    student=student,
                    teacher=teacher,
                    faculty_name=class_name,
                    class_room=class_room
                )
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'status': f'Class {class_name} assigned to teacher {teacher.first_name} in room {class_room}.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False)
    def active_teachers(self, request):
        """
        A custom action to get a list of active teachers.
        """
        active_teachers = Teacher.objects.filter(is_active=True)

        page = self.paginate_queryset(active_teachers)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(active_teachers, many=True)
        return Response(serializer.data)
