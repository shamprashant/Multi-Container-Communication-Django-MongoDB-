from django.http.response import HttpResponse
from django.shortcuts import render
import os
from pymongo import MongoClient
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html', context={'welcome_message': 'Welcome to the index page!!'})

def print_both(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        content = request.POST['content']
        with open(os.getcwd()+'/feedback/'+file_name+'.txt', 'w') as file:
            file.write(content)
            print(os.getcwd())
        client = MongoClient("mongodb://mongodb:27017/")
        db = client["customersdb"]
        customers = db["customers"]
        for x in customers.find():
            print(x)
    return render(request, 'basic_app/index.html', context={'welcome_message': 'Welcome to the index page!!'})

def show_file_data(request):
    file_name = request.path.split('/')[-1]
    
    try:
        with open(os.getcwd()+'/feedback/'+file_name) as file:
            content = file.read()
            return HttpResponse(content)
    except:
        return HttpResponse('No file found with the name ',file_name)

# docker run -p 8000:8000 --name django_app -v feedback:/app/feedback -v "/Users/prashant/Documents/python_files/assignment-problem/django-app:/app" django_image