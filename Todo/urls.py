from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_task',views.add_data), 
    path('delete/<int:id>',views.delete_task)   
]