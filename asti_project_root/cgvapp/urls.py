from django.urls import path
from . import views

urlpatterns = [
    path('cgv_list_employees/', views.ListEmployees.as_view(), name='cgv_list_employees'),
    path('cgv_create_employee/', views.CreateEmployee.as_view(), 	name='cgv_create_employee'),
    path('cgv_get_employee/<pk>/', views.EmployeeDetails.as_view(), name='cgv_get_employee'),
    path('cgv_update_employee/<pk>/', views.EmployeeUpdate.as_view(), name='cgv_update_employee'),
    path('cgv_delete_employee/<pk>/', views.EmployeeDelete.as_view(), name='cgv_delete_employee'),


]




#http://localhost:8000/cgvapp/cgv_list_employees/