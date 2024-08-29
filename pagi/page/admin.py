from django.contrib import admin
from .models import Student, Teacher, Subject, SubjectMarks, StudentFaculty

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'password')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('address',)

class StudentInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'roll_no')
    search_fields = ('first_name', 'last_name')
    inlines = [StudentInline]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(SubjectMarks)
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'marks')

@admin.register(StudentFaculty)
class StudentFacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'teacher', 'faculty_name', 'class_room', 'today_day', 'class_timing')
    list_filter = ('today_day', 'class_timing')
    search_fields = ('faculty_name', 'student__first_name', 'teacher__first_name')
    inlines = [StudentInline]

# Unregister the intermediate model from admin to avoid confusion
admin.site.unregister(Student.teachers.through)
