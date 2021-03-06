"""playbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'login/$', login, name='login'),
    url(r'logout/$','apps.accounts.views.logout', name='logout'),
    url(r'^logged/$','apps.accounts.views.logged'),
    url(r'^alliance/apps/backlog/', include('apps.backlog.urls')),
    url(r'^alliance/core/', include('apps.shared.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
]


