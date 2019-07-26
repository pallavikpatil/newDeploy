from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.
class Faculty(models.Model):
    code = models.IntegerField()
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    active=models.BooleanField()

    class Meta:
        db_table="faculty_info"