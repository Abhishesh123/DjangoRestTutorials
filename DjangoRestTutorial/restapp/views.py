from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from restapp.serialization import QuestionChoiceSerializer
from django.views.decorators.csrf import csrf_exempt
from restapp.models import *

 
# Create your views here.
def index(request):
    return HttpResponse("Hello API") 
@csrf_exempt
def choice_list(request):
    try:
        choice = Choice.objects.all()
    except Choice.DoesNotExist:
        return JsonResponse({"status": 404,"message": "Invalid id"})
    if request.method == 'GET':
        serializer = QuestionChoiceSerializer(choice, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif  request.method=='POST':
        data = JSONParser().parse(request)
        serializer.QuestionChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def choice_list_id(request, pk):
    try:
        choice=Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
        return JsonResponse({"status": 404,"message": "Invalid id"})
    if request.method=='GET':
        serializer=QuestionChoiceSerializer(choice)
        return JsonResponse(serializer.data)
