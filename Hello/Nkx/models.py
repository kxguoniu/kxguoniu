from django.db import models

# Create your models here.

class test(models.model):
    #id = models.AutoField()
    name = models.CharField(max_length=20)
    status = models.BooleanField()
    email = models.EmailField()
    number = models.BigIntegerField()
    text = models.TextField(null=True)
    data = models.DateField()
    time = models.DateTimeField()
    num = models.DecimalField()
    file = models.FileField()
