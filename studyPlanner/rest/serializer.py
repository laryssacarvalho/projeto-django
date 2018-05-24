from rest_framework import serializers

from studyPlanner.core.models import User, Class, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'ra']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['code', 'professor', 'examMod1', 'examMod2', 'examSub', 'room', 'weekDay', 'horario']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['idTaskType', 'data', 'name', 'file', 'taskClass']