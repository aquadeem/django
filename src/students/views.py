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
    new_person = Person()
    new_person.first_name = 'Anatoly'
    new_person.last_name = 'Kashpirovsky'
    new_person.age_person = 'none'
    new_person.type_person = 'Mage'
    new_person.create_person = 'none'
    new_person.update_person = 'none'
    new_person.status_person = 'Passive'
    new_person.save()

    """del_person = Person.objects.get(first_name='John')
    del_person.delete()"""

    return JsonResponse({'person': []})


def index_with_get(request):
    name = request.GET.get('name')
    if not name:
        name = 'stranger'
    return HttpResponse(f'Hello, {name}')