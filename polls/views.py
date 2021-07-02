from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from polls.models import Student
from polls.api.serializers import StudentSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_students(request):
    student_list = Student.objects.all()
    student_serializer = StudentSerializer(student_list, many=True)

    return JsonResponse(student_serializer.data, safe=False, status=status.HTTP_200_OK)