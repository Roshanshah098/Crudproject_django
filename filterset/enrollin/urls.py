from django.urls import path
from .views import StudentList  # Import StudentList view

# Define urlpatterns
urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list-filtered'),  # Add path for StudentList view
]



