from django.db import models

# Create your models here.
class UserInformation(models.Model):

    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40,null=True, blank=True)
    mobile = models.CharField(max_length=10,null=True, blank=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40,null=True, blank=True)
    token = models.CharField(max_length=40,null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class QuestionDetails(models.Model):
    userid = models.IntegerField(max_length=50,null=True,blank=True)
    description = models.TextField(max_length=500)
    question = models.TextField(max_length=5000)
    questionid =  models.IntegerField(max_length=50,null=True,blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class AnswerDetails(models.Model):
    userid = models.IntegerField(max_length=50,null=True,blank=True)
    questionid =  models.IntegerField(max_length=50,null=True,blank=True)
    answerid =  models.IntegerField(max_length=50,null=True,blank=True)
    answer =  models.TextField(max_length=5000)
    likescount = models.IntegerField(default=0) 
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    posted  = models.BooleanField(default=False)

    

