from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
