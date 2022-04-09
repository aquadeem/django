from django.db.models import Model, CharField

# Create your models here.


class Student(Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)


class Person(Model):

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age_person = CharField(max_length=50)
    type_person = CharField(max_length=50)
    create_person = CharField(max_length=50)
    update_person = CharField(max_length=50)
    status_person = CharField(max_length=50)