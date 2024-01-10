from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView
from .models import Employee
from django.urls import reverse_lazy

# Create your views here.
class ListEmployees(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'cgvapp/employee_list.html'
    success_url = reverse_lazy('cgv_list_employees')


class CreateEmployee(CreateView):
    model = Employee
    fields = ('empid', 'name', 'age', 'salary', 'address')
    #template_name = 'cgvapp/employee_form.html'
    success_url = reverse_lazy('cgv_list_employees')



class EmployeeDetails(DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'cgvapp/employee_details.html'





class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ('empid', 'name', 'age', 'salary', 'address')
    context_object_name = 'employee'
    template_name = 'cgvapp/employee_update_form.html'
    success_url = reverse_lazy('cgv_list_employees')


class EmployeeDelete(DeleteView):
    model = Employee

    # fields = ('empid', 'name', 'age', 'salary', 'address')

    context_object_name = 'employee'

    # NOTE: By default Django will search for "employee_confirm_delete.html" template file, if it is not present then error
    # template_name = 'cgvapp/employee_confirm_delete.html'
    success_url = reverse_lazy('cgv_list_employees')
