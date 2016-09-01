from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Group_info(models.Model):
	teacher = models.CharField(max_length=50)
	class_info = models.TextField()
	teacher_info =models.TextField()
	subject = models.CharField(max_length=50)
	groups_info = models.ManyToManyField(User)

# Create your models here.
class Suggestion(models.Model):
	suggestion=models.TextField()
	
class User_info(models.Model):
	gender=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	school=models.CharField(max_length=50)
	birthday=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	users_info=models.ManyToManyField(User)
