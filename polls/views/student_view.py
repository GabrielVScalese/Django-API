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

@api_view(['GET'])
def get_student(request, ra):
    student = Student.objects.get(pk=ra)  
    student_serializer = StudentSerializer(student)

    return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def insert_student(request):
    body = JSONParser().parse(request)
    student_serializer = StudentSerializer(data=body)

    if student_serializer.is_valid():
        student_serializer.save()   
        return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Error for insert student'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_student(request, ra):
    body = JSONParser().parse(request)
    student = Student.objects.get(pk=ra)
    student_serializer = StudentSerializer(instance=student, data=body)

    if student_serializer.is_valid():
        student_serializer.save()
        return JsonResponse(student_serializer.data, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Error for update student'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, ra):
    student = Student.objects.get(pk=ra)

    student.delete()

    return JsonResponse({'message': 'Deleted student'}, status=status.HTTP_200_OK)
