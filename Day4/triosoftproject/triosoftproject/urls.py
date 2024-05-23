"""
URL configuration for triosoftproject project.

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
from django.urls import include, path

#Importing all views 

# from triosoftproject import api_app
from triosoftproject.views import first_page, home_page, second_page, third_page


#home_page,first_page,Second_page,third_page function's is connected here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('first/', first_page),
    path('second/', second_page),
    path('third/',third_page),
    path('apiapp/v1/',include('api_app.urls'))
    
]
