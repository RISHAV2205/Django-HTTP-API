from django.urls import path
from .views import add_student,list_students,update_student, partial_update_student

urlpatterns = [
    path('add/', add_student),
    path('list/', list_students), 
    path('update/<int:pk>/', update_student),
    path('partial-update/<int:pk>/',partial_update_student)
]
