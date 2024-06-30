from django.db import models
from datetime import datetime

# Create your models here.

class Owners(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    # more fields here...

    def __str__(self):
        return self.name
    
class Deptos(models.Model):
    id = models.AutoField(primary_key=True)
    name_depto = models.CharField(max_length=30, null= False) 
    id_depto = models.IntegerField(unique=True, null=False)
    n_mpios = models.IntegerField(null=True)
    main_city = models.CharField(max_length=30, null=False)
    date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
    update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

    def __str__(self):
        return self.name_depto
    
class Mpios(models.Model):
    id = models.AutoField(primary_key=True)
    name_mpio = models.CharField(max_length=30, null= False) 
    id_mpio = models.IntegerField(unique=True, null=False)
    n_veredas = models.IntegerField(null=True)
    cabecera = models.CharField(max_length=30, null=False)
    date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
    update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

    def __str__(self):
        return self.name_mpio
