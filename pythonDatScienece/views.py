from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pythonDatScienece.serialize import *
from pythonDatScienece.models import *

# Create your views here.


class FacultyVset(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerial

