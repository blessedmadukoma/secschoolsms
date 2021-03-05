from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Principal(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  schoolName = models.CharField(max_length=200)
  phone = models.CharField(max_length=15)

  def __str__(self):
    return self.user.username

class Role(models.Model):
  roleName = models.CharField(max_length=15)
  
  def __str__(self):
    return self.roleName

class Staff(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  principal = models.ForeignKey(Principal, on_delete=models.CASCADE)
  role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
  subjectTeaching = models.CharField(max_length=20, default="None")
  
  def __str__(self):
    return self.user.username