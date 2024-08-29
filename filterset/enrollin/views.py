#from django_filters import rest_framework as filters
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
#per view setting
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter
from rest_framework import filters

# class StudentFilter(filters.FilterSet):
#     class Meta:
#         model = Student 
#         fields = {
#             'first_name': ['exact', 'icontains'],
#             'student_age': ['exact', 'gte', 'lte'],
#         }



class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request) 

class StudentList(generics.ListAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #filter_backends = [DjangoFilterBackend] 
    #filterset_class = StudentFilter 
    #filterset_fields = ['first_name']    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^first_name', 'student_age']      #starswith  
    filter_backends = [filters.OrderingFilter]
    ordering = ['first_name']            #default ordering 
    ordering_fields = '__all__' 
    

    # def get_queryset(self):
    #     user = self.request.user     #only login user data is shown
    #     return Student.objects.filter(passby=user)    #only login user data is shown
