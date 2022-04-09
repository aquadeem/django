from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from students.models import Student, Person
# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def students_json(request):
    students = Student.objects.all()
    return JsonResponse({'students': list(students)})

def person_json(request):
    person = Person.objects.all()
    return JsonResponse({'person': list(person)})


def index_with_get(request):
    name = request.GET.get('name')
    if not name:
        name = 'stranger'
    return HttpResponse(f'Hello, {name}')