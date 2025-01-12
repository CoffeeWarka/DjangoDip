"""
URL configuration for tester project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from quiz import views
from django.contrib.auth import views as dj_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('<int:question_id>quest/', views.choose_question, name='quest'),
    path('<int:question_id>/answer/', views.question_answer, name='answer'),
    path('<int:question_id>/user_choice/', views.user_choice, name='user_choice'),
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', dj_views.LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', dj_views.LogoutView.as_view(template_name='quiz/logout.html'), name='logout'),
]
