from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    yop=models.PositiveBigIntegerField()
    skill=models.CharField(max_length=100)
    percentage=models.PositiveIntegerField()
    mockRating=models.CharField(max_length=5)
