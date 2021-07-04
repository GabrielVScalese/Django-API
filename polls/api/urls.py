from django.urls import path

from polls.views import student_view

urlpatterns = [
    path('students', student_view.get_students), 
    path('students/<int:ra>', student_view.get_student),
    path('insertStudent', student_view.insert_student),
    path('updateStudent/<int:ra>', student_view.update_student),
    path('deleteStudent/<int:ra>', student_view.delete_student)
]