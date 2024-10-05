from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dept = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.dept

class Type(models.Model):
    type=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.type

class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    d_birth=models.DateField(null=True,blank=True,auto_now_add=False)
    gen=models.CharField(max_length=30,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    add=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
class Status(models.Model):
    status=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status

class Uploadfile(models.Model):
    status=models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    emp=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    sub=models.CharField(max_length=100,null=True)
    des=models.CharField(max_length=500,null=True)
    file=models.FileField(null=True)

    def __str__(self):
        return self.sub
