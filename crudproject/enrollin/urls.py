from django.urls import path
from . import views


    #path('students/', ListCreateAPIView.as_view(queryset=Student.objects.all(), serializer_class=StudentSerializer), name='student-list-create'),
urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students_create/', views.student_create, name='student_create'),
    path('students_update/<int:pk>/', views.student_update, name='student_update'),
    path('students_delete/<int:pk>/', views.student_delete, name='student_delete'),
]



