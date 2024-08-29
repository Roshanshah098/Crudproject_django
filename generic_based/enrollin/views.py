#from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
#from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()  
    serializer_class = StudentSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentDetail(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

        
        
    
    
    
   #exta code just pratice set
    
# class StudentListCreate(generics.ListCreateAPIView): #read-write concerete view classes
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer  
#     permission_classes = [IsAdminUser]  

#     def create(self, request, *args, **kwargs):   
#         serializer = self.get_serializer(data=request.data) 
#         serializer.is_valid(raise_exception=True)   
#         self.perform_create(serializer) 
#         headers = self.get_success_headers(serializer.data)
#         return Response({'msg': 'Data Created', 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
    
# class StudentUpdateView(generics.UpdateAPIView):  #update-only 
#     queryset = Student.objects.all()  
#     serializer_class = StudentSerializer
#     permission_classes = [IsAdminUser]  

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'msg': 'Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)

# class StudentDeleteView(generics.DestroyAPIView):  #delete only 
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [IsAdminUser]
 
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
    


    
    
    
    