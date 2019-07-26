from rest_framework.serializers import ModelSerializer
from pythonDatScienece.models import *

class FacultySerial(ModelSerializer):
    class Meta:
        model = Faculty
        fields= '__all__'
