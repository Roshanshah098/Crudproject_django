from rest_framework import viewsets, mixins, generics,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer 

# class StudentViewSet(viewsets.ViewSet):
#     queryset = Student.objects.all() 
#     serializer_class = StudentSerializer 

#     def list(self, request):  
#         students = self.queryset  
#         serializer = self.serializer_class(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)  

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         return Response({'msg': 'Data Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None): 
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(student, data=request.data)
#         if serializer.is_valid():  
#             serializer.save() 
#             return Response({'msg': 'Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         student = get_object_or_404(self.queryset, pk=pk)
#         student.delete()
#         return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)


# generic viewset as custom viewset >>
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly
from .custompermissions import MyPermission 
#from .customauth import CustomAuthToken
from .customauthenticate import CustomAuthentication


class StudentViewSet(viewsets.GenericViewSet,  
                     mixins.CreateModelMixin, 
                     mixins.ListModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 
    authentication_classes = [CustomAuthentication, TokenAuthentication]  
    permission_classes = [MyPermission]   

    
    # Override the partial_update method
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response({  
            'status': 'success', 
            'message': 'Student partially updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK) 
        

    # Override the update method
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Student updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
