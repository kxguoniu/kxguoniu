from django.db import models

# Create your models here.

class test(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=20)
    status = models.BooleanField()
    email = models.EmailField()
    number = models.BigIntegerField()
    text = models.TextField(null=True)
    data = models.DateField()
    time = models.DateTimeField()
    num = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField()
