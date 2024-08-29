
from django import forms   
from .models import Teacher , Student

class Teacherregistration(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'password', 'email', 'phone', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'image']

    teacher_relation = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Teachers",
    )
    
    