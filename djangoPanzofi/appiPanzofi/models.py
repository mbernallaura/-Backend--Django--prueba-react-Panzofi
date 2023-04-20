from django.db import models

# Create your models here.
class panzofi (models.Model): 
    cod_panzofi= models.AutoField(primary_key=True)
    logo= models.BinaryField(null=True)
    title= models.CharField(max_length=10)
    description= models.CharField(max_length=400)

class rol (models.Model):
    cod_rol= models.AutoField(primary_key=True)
    name= models.CharField(max_length=10)

class usuario (models.Model):
    cod_id= models.AutoField(primary_key=True)
    cod_rol= models.ForeignKey(rol, on_delete=models.CASCADE, blank=False)
    user= models.CharField(max_length=100, unique=True)
    password= models.CharField(max_length=40)
    date_session= models.DateTimeField(null=True)
    time_session= models.TimeField(null=True)
    button1= models.IntegerField(null=True)
    button2= models.IntegerField(null=True)
    