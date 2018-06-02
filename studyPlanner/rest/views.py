from django.http import JsonResponse

from studyPlanner.core.models import User, Class, Task
from studyPlanner.rest.serializer import UserSerializer, ClassSerializer

def api_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

def api_classes(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)
    return JsonResponse(serializer.data, safe=False)

def api_tasks(request):
    tasks = Task.objects.all()
    serializer = ClassSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)
