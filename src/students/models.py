from django.db.models import Model, CharField

# Create your models here.


class Student(Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
