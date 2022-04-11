# Generated by Django 4.0.3 on 2022-04-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_person_age_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('course_name', models.CharField(max_length=50)),
                ('course_type', models.CharField(default='Offline', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(max_length=50)),
                ('group_city', models.CharField(max_length=50)),
                ('group_amount', models.IntegerField(default='0')),
                ('group_type', models.CharField(default='Offline', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('lesson_name', models.CharField(max_length=50)),
                ('lesson_type', models.CharField(default='Practice', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_level', models.CharField(default='Novice', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
