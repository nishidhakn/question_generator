from django.db import models

# Create your models here.
Class_choices = (
    (7, 7),
    (8, 8),
    (9, 9),
)
Subject_choices = (
    ("Physics", "Physics"),
    ("Chemistry", "Chemistry"),
    ("Biolodgy", "Biolodgy"),   
    
)
Question_choices = (
    ("twomark", "twomark"),
    ("threemark", "threemark"),
    ("fivemark", "fivemark"),   
    
)

class Question(models.Model):
	class1=models.IntegerField(choices=Class_choices,verbose_name='class')
	subject=models.CharField(max_length=20,choices=Subject_choices)
	questiontype=models.CharField(max_length=20,choices=Question_choices)
	question=models.CharField(max_length=250)
