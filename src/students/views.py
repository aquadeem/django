from django.http import HttpResponse, JsonResponse
from students.models import Student
# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def students_json(request):
    students = Student.objects.all()
    return JsonResponse({'students': list(students)})


def index_with_get(request):
    name = request.GET.get('name')
    if not name:
        name = 'stranger'
    return HttpResponse(f'Hello, {name}')
