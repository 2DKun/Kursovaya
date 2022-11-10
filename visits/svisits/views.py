from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

import svisits
from .models import Student, Visits
from .serializers import SSerializer, VSerializer


# Create your views here.

@csrf_exempt
def StudentApi(request, id=0):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = SSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        students_serializer = SSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(student_id=student_data['student_id'])
        students_serializer = SSerializer(student, data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        student = Student.objects.get(student_id=id)  # из URL
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)
