from django.db import models
class customers(models.Model):
    name=models.CharField(max_length=100)
    room_num=models.IntegerField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    date=models.models.DateField()

class room(models.Model):
    room_name=models.CharField(max_length=100)
    room_num=models.models.IntegerField()
# Create your models here.
