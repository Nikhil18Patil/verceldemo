from django.db import models



class nik(models.Model):
    name=models.CharField(max_length=50)
    village=models.CharField(max_length=50)
      
    def __str__(self):
        return self.title  

# Create your models here.
