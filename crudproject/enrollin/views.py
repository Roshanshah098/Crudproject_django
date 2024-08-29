from django.shortcuts import render,redirect,get_object_or_404
from .models import Teacher,Student #Subject_marks,Subject,StudentFaculty  #StudentFaculty
from .forms import Teacherregistration ,StudentForm
# Create your views here.
## return render(request,'base.html')


#this function will add new item and view items
def add_show(request):
    if request.method =="POST":
        form=Teacherregistration(request.POST)
        if form.is_valid():
            #field = form.cleaned_data['fields']     
            #field.save() 
            
            nm = form.cleaned_data['first_name']
            lm = form.cleaned_data['last_name'] 
            pw = form.cleaned_data['password'] 
            em = form.cleaned_data['email'] 
            pn = form.cleaned_data['phone']
            ad = form.cleaned_data['address']
            reg = Teacher(first_name = nm, last_name = lm, password= pw, email = em, phone=pn, address= ad)
            reg.save()  #database maah save vvayo
            form=Teacherregistration()   #fields become blank after got saved in database
    else:  
        form=Teacherregistration()
    teacher = Teacher.objects.all()  #after adding data , it will refresh it to empty-space
    # print("Hello",student)
            
    return render(request, 'enrollin/addandview.html',{'form' : form, 'teacher' : teacher})

# this function will Update/edit
def update_data(request, id):
    pi = get_object_or_404(Teacher, pk=id) 
    if request.method == "POST":
        form = Teacherregistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('add_show')  # Redirect to the main page after saving
    else:
        form = Teacherregistration(instance=pi)
    return render(request, 'enrollin/updatestudent.html', {'form': form})

# This function will delete 
def delete_data(request, id):
    if request.method == "POST":
        pi = get_object_or_404(Teacher, pk=id)
        pi.delete()
        return redirect('/')
    
    
# This function will add new student and view students
# def add_and_view(request):
#     if request.method == "POST":
#         form = Teacherregistration(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_and_view')
#     else:
#         form = Teacherregistration()

#     teachers = Teacher.objects.all()
#     students = Student.objects.all()
#     return render(request, 'enrollin/addandview.html', {'form': form, 'teachers': teachers, 'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('add_show')  # Ensure this is the correct redirect URL name
    else:
        form = StudentForm()
    return render(request, 'enrollin/add_new_student.html', {'form': form})  

#from django.db.models import Q, Sum  #or condtion

# def get_student(request):  #{{forloop.counter}} used in template to fix pagenumber and 
#     #also import in views.py django pagination to fix page 
#     students = Student.objects.all() 
    
#     ranks = Student.objects.annotate(marks = Sum())
    
#     if request.Get.get('search'):
#         search = request.GET.get('search')
#         student = student.filter(
#             Q(first_name__icontains = search) |
#             Q(last_name__icontains = search) |
#             Q(teachers__first_name__icontains = search) 
            
#         )  
        
#     return render(request, 'enrollin/get_student.html', {'students': students})

# def see_marks(request, id):   
#     queryset = Subject_marks.objects.filter(student__id = id)  
#     total_marks = queryset.aggregate(total_marks = Sum('marks')) 
#     return render(request, 'enrollin/see_marks.html', {'queryset': queryset}, {'total_marks': total_marks})

def view_student_detail(request, id):  
    student = get_object_or_404(Student, id=id)
    return render(request, 'enrollin/student_detail.html', {'student': student})


# serializer logic view :
# from rest_framework import serializers

#create student_create logic >>
# from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():   #request.data returns parsed content of request body.
        serializer.save()
        res = {'msg': 'Data Created', 'data': serializer.data}
        return Response(res, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#request.query_params , similar to request.GET )
@api_view(['GET'])     
def student_list(request): 
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def student_update(request, pk): 
    student = get_object_or_404(Student, pk=pk) 
    serializer = StudentSerializer(student, data=request.data, partial = True)
    if serializer.is_valid(): 
        serializer.save() 
        return Response({'msg': 'Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)



# generic class based -> view logic  
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'msg': 'Data Created', 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

class StudentUpdateView(generics.UpdateAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False) 
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'msg': 'Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]
 
    def destroy(self, request, *args, **kwargs):  
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
