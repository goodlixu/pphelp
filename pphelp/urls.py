"""pphelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from core import views as core_views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^accounts/login/$',auth_views.login,{'template_name':'login.html'}),
    url(r'^admin/', admin.site.urls),
	url(r'^$',core_views.index),
	url(r'^login',core_views.login_views),
	url(r'^user_center',core_views.user_center),
	url(r'^class',core_views.class_info),
	url(r'^register',core_views.register),
	url(r'^teacher',core_views.teacher_list),
	url(r'^suggestion',core_views.suggestion),
	url(r'^appoint',core_views.appoint),
	url(r'^change_info',core_views.change_info),
]
