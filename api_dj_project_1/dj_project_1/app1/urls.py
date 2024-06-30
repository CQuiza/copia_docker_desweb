"""
URL configuration for dj_project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app1 import viewsLog, viewsOwner, viewsDeptos, viewsMpios
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'owners', viewsOwner.OwnerViews, 'owners')
router.register(r'deptos', viewsDeptos.DeptosViews, 'deptos')
router.register(r'mpios', viewsMpios.MpiosViews, 'mpios')


urlpatterns = [
    
    re_path('login/', viewsLog.login),
    re_path('register/', viewsLog.register),
    re_path('profile/', viewsLog.profile),
    re_path('logout/', viewsLog.logout),

    path('owners/', include(router.urls)),
    path('deptos/', include(router.urls)),
    path('mpios/', include(router.urls)),

    path('docs/', include_docs_urls(title='API Documentation')),
]