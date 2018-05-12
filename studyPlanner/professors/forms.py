from django import forms
from studyPlanner.students.models import Student_Exam, Task_Student

class Student_ExamForm(forms.ModelForm):
    class Meta:
        model = Student_Exam
        fields = ('student', 'examClass','gradeMod1', 'gradeMod2', 'gradeSub')
        readonly = ('student', 'examClass')

class Task_StudentForm(forms.ModelForm):
    class Meta:
        model = Task_Student
        fields = ('task', 'student', 'file','grade')