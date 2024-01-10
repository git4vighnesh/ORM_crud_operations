from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.create_employee),
    path('list_emp/', views.list_employees),
    path('delete_emp/', views.delete_emp),
    path('ems/', views.ems),
    path('update_employee/<pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<pk>/', views.delete_employee, name='delete_employee'),

]



# http://localhost:8000/empapp/employee/

# http://localhost:8000/empapp/list_emp/

# http://localhost:8000/empapp/delete_emp/