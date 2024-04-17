from django.db import models
from django.contrib.auth.models import User



    

class semester_info(models.Model):
    uni_id=models.IntegerField(default=0)
    semester=models.IntegerField(default=0)
    roll = models.CharField(max_length=100,default=0)
    year=models.IntegerField()
    branch=models.CharField(max_length=50,default="")
     
    

    

group_choices = (
    ("A","A"),
    ("B","B"),
    ("C","C"),
    ("D","D"),
    ("E","E"),
    ("F","F"),
    ("G","G"),
    ("H","H")
)

class Database(models.Model):
    sem=models.IntegerField(default=0)
    branch=models.CharField(max_length=100,default="")
    Group=models.CharField(choices=group_choices,max_length=50,default=None)
    course_name1=models.CharField(max_length=100,default="")
    course_name2=models.CharField(max_length=100,default="")
    course_name3=models.CharField(max_length=100,default="")
    course_name4=models.CharField(max_length=100,default="")
    
    