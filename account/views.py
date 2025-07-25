from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views import View
from .models import Student
from .crypto_utils import encrypt_password, decrypt_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):
    # POST = Register Student (with encrypted password)
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        encrypted = encrypt_password(password)
        student, created = Student.objects.update_or_create(
            email=email,
            defaults={'name': name, 'encrypted_password': encrypted}
        )
        return JsonResponse({'message': 'Student registered successfully'}, status=201)

    # GET = Retrieve decrypted password by email
    def get(self, request, email=None):
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        try:
            student = Student.objects.get(email=email)
            decrypted = decrypt_password(student.encrypted_password)
            return JsonResponse({
                'name': student.name,
                'email': student.email,
                'password': decrypted
            })
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET', 'POST'])
