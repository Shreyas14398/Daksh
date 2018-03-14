# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from jobss.forms import CreateU
from jobss.forms import LoginF
from jobss.forms import LoginR
from jobss.forms import LoginP
from jobss.forms import SkillP
from jobss.models import UserObj
from jobss.models import RecObj

# Create your views here.

def home(request):
  return render(request,"home.html",{})

def signup(request):
   userobj="0"
   if request.POST:
      MyUserForm=CreateU(request.POST)
   if MyUserForm.is_valid():
      userobj=UserObj(name=MyUserForm.cleaned_data['name'],email=MyUserForm.cleaned_data['email'],uname=MyUserForm.cleaned_data['uname'], password=MyUserForm.cleaned_data['password'])
      userobj.save()
      return render(request,"base.html",{"message":"Registered Successfully!"}) 
   else:
      MyUserForm=CreateU()
      return render(request,"base.html",{"message":"We encountered a small problem! Please try again!"}) 


def user(request):
  useobj="0"
  if request.POST:
    MyUseForm=LoginF(request.POST)
    if MyUseForm.is_valid():
     dbN=UserObj.objects.get(uname=MyUseForm.cleaned_data['uname'])
     return render(request,'main1.html',{"name":dbN.name})
    else:
     return render(request,"base.html",{"message":"Invalid Username or Password"}) 
  else:
    return render(request,'base.html',{})

def recru(request):
  useobj="0"
  if request.POST:
    MyUseForm=LoginR(request.POST)
    if MyUseForm.is_valid():
     dbN=RecObj.objects.get(uname=MyUseForm.cleaned_data['uname'])
     return render(request,'main2.html',{"name":dbN.company})
    else:
     return render(request,"base.html",{"message":"Invalid Username or Password"}) 
  else:
   return render(request,"base.html",{})

def profile(request):
   if request.POST:
     MyUseForm=LoginP(request.POST)
     if MyUseForm.is_valid():
      dbN=UserObj.objects.get(password=MyUseForm.cleaned_data['password'])
      return render(request,'profile.html',{"name":dbN.name, "email":dbN.email, "uname":dbN.uname, "message":dbN.message, "skill1":dbN.skill1, "skill2":dbN.skill2, "skill3":dbN.skill3})
   else:
    return render(request,"home.html",{})

def skills(request):
   if request.POST:
     MyUseForm=SkillP(request.POST)
     if MyUseForm.is_valid():
      dbN=UserObj.objects.get(password=MyUseForm.cleaned_data['password'])
      dbN.skill1=MyUseForm.cleaned_data['skill1']
      dbN.skill2=MyUseForm.cleaned_data['skill2']
      dbN.skill3=MyUseForm.cleaned_data['skill3']
      dbN.save()
      return render(request,'profile.html',{"name":dbN.name, "email":dbN.email, "uname":dbN.uname, "message":dbN.message, "skill1":dbN.skill1, "skill2":dbN.skill2, "skill3":dbN.skill3})
   else:
     return render(request,"home.html",{})


def jobs(request):
    return render(request,"jobs.html",{})

def tech(request):
    return render(request,"tech.html",{})

def nontech(request):
    return render(request,"nontech.html",{})

def interns(request):
    return render(request,"intern.html",{})

