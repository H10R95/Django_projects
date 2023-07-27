import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from student.models import Student
from django.http import JsonResponse
from student_portal.settings import BASE_DIR
import os
import json

@csrf_exempt

def register(request):
   if request.method == "POST":
       resp_obj = Student.objects.create(name=request.POST.get('name'),
                                         rollnumber=request.POST.get('rollnumber'),
                                         mail_id=request.POST.get('mail_id'),
                                         password=request.POST.get('password'),
                                         dob=request.POST.get('dob'))

       return redirect('Login')
   return render(request,'Student.html')





def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        name = request.POST['name']
        mail_id = request.POST['mail_id']

        try:
            check = Student.objects.get(password=password, name=name, mail_id=mail_id)

            b = {'m': 'login success'}
            return JsonResponse(b)
        except Student.DoesNotExist:
            b = {'error': 'Invalid credentials'}
            return JsonResponse(b)

    return render(request, 'login.html')










