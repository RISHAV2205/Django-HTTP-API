from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('students/', StudentAPIView.as_view()),
    path('students/<int:pk>/', StudentAPIView.as_view()),
]
