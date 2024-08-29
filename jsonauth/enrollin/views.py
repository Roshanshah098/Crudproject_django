from rest_framework import viewsets, mixins
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from enrollin.throttling import randomuser
#ScopedRateThrottle ,in  throttle_scope which defined classes;

class StudentViewSet(viewsets.GenericViewSet,  
                     mixins.CreateModelMixin,  
                     mixins.ListModelMixin, 
                     mixins.RetrieveModelMixin, 
                     mixins.UpdateModelMixin): 
    queryset = Student.objects.all()   
    serializer_class = StudentSerializer  
    authentication_classes = [SessionAuthentication]    
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, randomuser]  

