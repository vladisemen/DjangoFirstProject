"""DjangoFirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, paths
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from firstapp import views
 
urlpatterns = [

    path('index.html/men.html', views.men),

    path('', views.index), #запрос к индексу обрабатывается def index
    re_path(r'^index', views.index), #запрос к about обрабатывается def
    re_path(r'^about', views.about),
    re_path(r'^men', views.men),
    re_path(r'^admin', views.admin),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),

]
