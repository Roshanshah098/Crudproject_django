from django.urls import path
from .views import StudentList, StudentCreate, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students_create/', StudentCreate.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('students_update/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    path('students_delete/<int:pk>/', StudentDelete.as_view(), name='student-delete'),
]
