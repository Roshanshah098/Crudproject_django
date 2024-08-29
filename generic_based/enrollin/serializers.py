from rest_framework import serializers
#from rest_framework.validators import UniqueTogetherValidator
from .models import Student, Teacher, Subject, Subject_marks, StudentFaculty

class TeacherSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Teacher
            fields = "__all__" 
            
class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)

    
    class Meta:  
        model = Student 
        fields = ['id', 'first_name', 'last_name', 'image', 'student_rollno', 'student_age', 'teachers']
        extra_kwargs = { 'teachers': {'read_only' :True}}  #
        # validators = [  
        #     UniqueTogetherValidator(
        #         queryset=Student.objects.all(),
        #         fields=('student_rollno', 'first_name', 'last_name')
        #     )
        # ]
    # filed level validators
    def validate_student_rollno(self, value):   
        if value < 0:
            raise serializers.ValidationError("Roll number cannot be negative")
        return value 
    
    def create(self, validated_data):   
        teachers_data = validated_data.pop('teachers')
        student = Student.objects.create(**validated_data)
        for teacher_data in teachers_data:
            teacher, created = Teacher.objects.get_or_create(**teacher_data)
            student.teachers.add(teacher)   #add in manytomany fields >>
        return student       

    def update(self, instance, validated_data):
        teachers_data = validated_data.pop('teachers', None)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image = validated_data.get('image', instance.image)
        instance.student_rollno = validated_data.get('student_rollno', instance.student_rollno)
        instance.student_age = validated_data.get('student_age', instance.student_age)
        if teachers_data is not None:
            instance.teachers.clear()
            for teacher_data in teachers_data:
                teacher, created = Teacher.objects.get_or_create(**teacher_data)
                instance.teachers.add(teacher)
        instance.save()  
        return instance   
    
     

    
    





#     #  #Overriding .save()
#     # def save(self): 
#     #     data = self.validated_data
#     #     student = Student(name=data['name'], age=data['age'], rollno=data['rollno'])
    
# #for serialzer objects where data is being displyed; 
# #if object is many as eg: std = Student.objects.all()
# #serializer = SrudentSerialier(stdata, many = True) many = True when objects are many;
# # serializer = StudentSerializer()  
# # serializer.data  

# #if needed :
# #return HttpResponse(data, content_type = 'application/json')
# #return JsonResponse(data, safe = False) #safe; non-dict , false or dict then true

# from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io

# # Serialize a single student instance
# student_instance = Student.objects.first()
# serializer = StudentSerializer(student_instance)
# json_data = JSONRenderer().render(serializer.data)
# #print("Serialized JSON data:", json_data)

# # Return the serialized JSON data in an HttpResponse
# response = HttpResponse(json_data, content_type='application/json')
# #print("HttpResponse with JSON data:", response.content)

# # Deserialize the JSON data
# stream = io.BytesIO(json_data)
# data = JSONParser().parse(stream)
# #print("Deserialized data:", data)

# # Validate the deserialized data  
# serializer = StudentSerializer(data=data)
# if serializer.is_valid(raise_exception=True):  # Shows the boolean expression
#     validated_data = serializer.validated_data
#     #print("Validated data:", validated_data) 
    
#     # Return the validated data in a JsonResponse
#     response = JsonResponse(validated_data, safe=False)
#     print("JsonResponse with validated data:", response.content)
# else:
#     print("Errors:", serializer.errors)

# # For restoring data types into a dictionary of validated data
# serializer = StudentSerializer(data=data)
# serializer.is_valid(raise_exception=True)  # Shows the boolean expression
# restored_validated_data = serializer.validated_data
# #print("Restored validated data:", restored_validated_data)

# # Return the restored validated data in a JsonResponse
# response = JsonResponse(restored_validated_data, safe=False)
# #print("JsonResponse with restored validated data:", response.content)

