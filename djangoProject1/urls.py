"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from workerSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/', views.department),

    # 部门管理
    path('add/department/', views.department_add),
    path('department/delete/', views.department_delete),
    path('department/<int:nid>/edit/', views.department_edit),

    # 用户管理
    path('user/list/', views.user),
    path('user/add/', views.user_add),
    path('user/add/model/', views.user_add_model_form),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),

]
