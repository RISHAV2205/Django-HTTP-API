from django.urls import path
from .views import StudentView

urlpatterns = [
    path('', StudentView.as_view()),              
    path('<str:email>/', StudentView.as_view()),  
]
