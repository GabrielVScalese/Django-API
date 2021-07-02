from django.urls import path

from polls import views

urlpatterns = [path('students', views.get_students), path('insertStudent', views.insert_student)]