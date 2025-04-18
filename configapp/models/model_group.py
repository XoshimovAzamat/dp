from .auth_users import *
from .model_teacher import *
from django.db import models


class Room(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class TableType(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Table(BaseModel):
    start_time = models.TimeField()
    finish_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)
    type = models.ForeignKey(TableType, on_delete=models.RESTRICT)
    descriptions = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.start_time.__str__() + " " + self.end_time.__str__()


class GroupStudent(BaseModel):
    title = models.CharField(max_length=40, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='group_courses')
    teacher = models.ManyToManyField(Teacher, related_name='teacher_get')
    table = models.ForeignKey(Table, on_delete=models.RESTRICT)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.title
