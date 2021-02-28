from django.contrib import admin
from django.contrib.auth.models import User as user
from django.db import models
from django.db.models.base import Model 

from allauth.socialaccount.models import SocialAccount

from django.db.models.deletion import CASCADE

class User(models.Model):    
    id = models.IntegerField(null=False,primary_key=True)   
    usr = models.ForeignKey(to=user,on_delete=CASCADE,null=True,related_name='usr')  
    

class Doctor(models.Model):
    usr = models.ForeignKey(to=user,on_delete=CASCADE,null=True,related_name='doctor')  
    id = models.IntegerField(null=False,primary_key=True) 
    social  = models.ForeignKey(to=SocialAccount,on_delete=CASCADE,null=True,related_name='social')
    hospital = models.CharField(max_length=20,null=True)
    phno = models.CharField(max_length=15,null=True)
    pincode = models.CharField(max_length=6,null=True)
    sp = models.CharField(max_length=20,null=True)
    lno = models.CharField(max_length=20,null=True)
    online = models.BooleanField(default=False)    

class forum(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField(null=True,blank=True,default='unanswerd')
    
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(forum)
