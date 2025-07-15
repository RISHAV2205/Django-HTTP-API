from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status

from .models import Student   # this help when we are trying to get data


# Create your views here.
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student added", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()  # Get all student records
    serializer = StudentSerializer(students, many=True)  # many=True for a list
    return Response(serializer.data)  # Return JSON response

@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student updated", "data": serializer.data}, status=200)
    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def partial_update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    # 🔑 Only partially update the object
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student partially updated", "data": serializer.data}, status=200)
    return Response(serializer.errors, status=400)




