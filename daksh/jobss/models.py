# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserObj(models.Model):
  name=models.CharField(max_length=30)
  email=models.CharField(max_length=50)
  uname=models.CharField(max_length=30)
  password=models.CharField(max_length=30)
  skill1=models.CharField(max_length=30)
  skill2=models.CharField(max_length=30)
  skill3=models.CharField(max_length=30)
  message=models.CharField(max_length=30)
  appln=models.CharField(max_length=30)

  class Meta:
   db_table="UserObjs"

class RecObj(models.Model):
  name=models.CharField(max_length=30)
  email=models.CharField(max_length=50)
  company=models.CharField(max_length=50)
  uname=models.CharField(max_length=30)
  password=models.CharField(max_length=30)
  applns=models.CharField(max_length=30)

  class Meta:
   db_table="RecObjs"
