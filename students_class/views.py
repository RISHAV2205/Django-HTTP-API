from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Reuse the Student model from your original app
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student created", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student updated", "data": serializer.data})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({"message": "Student deleted"}, status=204)