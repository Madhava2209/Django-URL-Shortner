from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class url(models.Model):
    long_url=models.CharField(max_length=200,null=True,blank=True)
    title=models.CharField(max_length=100)
    short_hash=models.CharField(max_length=200,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    no_clicks=models.IntegerField(default=0)
    def __str__(self):
        return self(title) 