"""daksh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from jobss.views import home
from django.views.generic import TemplateView
from jobss.views import user
from jobss.views import recru
from jobss.views import signup
from jobss.views import profile
from jobss.views import skills
from jobss.views import jobs
from jobss.views import interns
from jobss.views import tech
from jobss.views import nontech

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',home),
    url(r'^login/',TemplateView.as_view(template_name="base.html")),
    url(r'^user/',user),
    url(r'^recru/',recru),
    url(r'^signup/',signup),
    url(r'^pro/',TemplateView.as_view(template_name="pro.html")),
    url(r'^profile/',profile),
    url(r'^skills/',skills),
    url(r'^jobs/',jobs),
    url(r'^interns/',interns),
    url(r'^tech/',tech),
    url(r'^nontech/',nontech),
]
