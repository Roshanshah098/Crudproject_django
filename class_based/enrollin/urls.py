from django.urls import path
from .views import StudentView

urlpatterns = [
    path('students/', StudentView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentView.as_view(), name='student-detail'),
]
