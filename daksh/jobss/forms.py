from django import forms
from jobss.models import UserObj
from jobss.models import RecObj
class CreateU(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.CharField(max_length=50)
    uname=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())

class LoginF(forms.Form):
    uname=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_uname(self):
     uname=self.cleaned_data.get("uname")
     dbn=UserObj.objects.filter(uname=uname)
     if not dbn:
       raise forms.ValidationError("Incorrect Username")
     else:
       return uname

    def clean_password(self):
      uname=self.cleaned_data.get("uname")
      password=self.cleaned_data.get("password")
      dbn=UserObj.objects.filter(uname=uname)
      if not dbn:
       raise forms.ValidationError("Incorrect Username")
      else:
       dbm=UserObj.objects.get(uname=uname)
       dbp1=dbm.password
       dbp=(password==dbp1)
       if not dbp:
         raise forms.ValidationError("Incorrect Password")
       else:
         return password

class LoginR(forms.Form):
    uname=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_uname(self):
     uname=self.cleaned_data.get("uname")
     dbn=RecObj.objects.filter(uname=uname)
     if not dbn:
       raise forms.ValidationError("Incorrect Username")
     else:
       return uname

    def clean_password(self):
      uname=self.cleaned_data.get("uname")
      password=self.cleaned_data.get("password")
      dbn=RecObj.objects.filter(uname=uname)
      if not dbn:
       raise forms.ValidationError("Incorrect Username")
      else:
       dbm=RecObj.objects.get(uname=uname)
       dbp1=dbm.password
       dbp=(password==dbp1)
       if not dbp:
         raise forms.ValidationError("Incorrect Password")
       else:
         return password

class LoginP(forms.Form):
     password=forms.CharField(widget=forms.PasswordInput())

class SkillP(forms.Form):
     skill1=forms.CharField(max_length=30)
     skill2=forms.CharField(max_length=30)
     skill3=forms.CharField(max_length=30)
     password=forms.CharField(widget=forms.PasswordInput())
