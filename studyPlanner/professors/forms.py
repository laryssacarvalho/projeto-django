from django import forms
from studyPlanner.students.models import Student_Exam

class Student_ExamForm(forms.ModelForm):
    class Meta:
        model = Student_Exam
        fields = ('student', 'examClass','gradeMod1', 'gradeMod2', 'gradeSub')