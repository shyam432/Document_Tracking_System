"""Document_Tracking_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from file.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_login', employee_login, name='loginemployee'),
    path('logout',Logout,name='logout'),
    path('', Home, name='home'),
    path('admin_sign',Admin_Sign,name='admin_sign'),
    path('employee_login', employee_login, name='loginemployee'),
    path('view/', viewdata, name='viewdata'),
    path('add_employee',Add_Employee,name='add_employee'),
    path('uploadfile',uploadfile,name='uploadfile'),
    path('viewfile/', viewfile, name='viewfile'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('viewstatus/',viewstatus,name='viewstatus'),
    path('c_password/',change_password,name='c_password'),
    path('delete_file/(?P<pid>[0-9]+)',delete_file,name='delete_file'),
    path('change_status/(?P<pid>[0-9]+)',change_status,name='change_status'),
    path('editview/(?P<pid>[0-9]+)',edit_employee,name='editview'),
    path('delete_view/(?P<pid>[0-9]+)',delete_view,name='delete_view'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
