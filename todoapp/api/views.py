from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View:': 'task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/taks-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskView(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailTaskView(request, **kwargs):
    task = Task.objects.get(id=kwargs['pk'])
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateTask(request, **kwargs):
    task = Task.objects.get(id=kwargs['pk'])
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, **kwargs):
    task = Task.objects.get(id=kwargs['pk'])
    task.delete()

    return Response()
