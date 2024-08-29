from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
#from rest_framework.authtoken.views import obtain_auth_token  function based;
from enrollin.customauth import CustomAuthToken

# Initialize the router and register the viewset
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

# Define urlpatterns by including router URLs
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view())
    #path('gettoken/', obtain_auth_token)  # will return json response
    #path('auth/', include('rest_framwork.urls',namespace='rest_framework'))  #for session authentication;
] 




# # Create view instances for specific actions
# student_list = StudentViewSet.as_view({'get': 'list', 'post': 'create'})
# student_detail = StudentViewSet.as_view({'get': 'retrieve'})
# student_update = StudentViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
# student_del = StudentViewSet.as_view({'delete': 'destroy'})

# # Define urlpatterns explicitly 
# urlpatterns = [
#     path('students/', student_list, name='student-list'),
#     path('students/<int:pk>/', student_detail, name='student-detail'),
#     path('students_update/<int:pk>/', student_update, name='student-update'),
#     path('students_delete/<int:pk>/', student_del, name='student-delete'),
# ]