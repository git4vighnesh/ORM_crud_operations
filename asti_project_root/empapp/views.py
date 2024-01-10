from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def create_employee(request):
    #How to check incoming request is GET/POST
    if request.method == 'GET':
        return render(request, 'empapp/employee_form.html')
    elif request.method == 'POST':
        #step1 : read employee
        empid = request.POST.get('emp_id')
        name = request.POST.get('emp_name')
        age = request.POST.get('emp_age')
        salary = request.POST.get('emp_salary')
        address = request.POST.get('emp_address')


        #step2: create "Employee model" object using employee input data
        employee = Employee(empid=empid, name=name, age=age, salary=salary, address=address)


        #step3: call save() method on "employee model" object
        employee.save()


        #step4: return response to the client using employee created successfully
        return HttpResponse("<h1 style='color: green'>Employee created!!!</h1>")

def list_employees(request):
    #STEP-1: x = Get all employees from Database table(EMPLOYEE) ===> QuerySet
    ### employees = {emp1, emp2}
    employees_db = Employee.objects.all()

    # STEP-2 - Create Context object(dict) with QuerySet
    context_data = {
        "employees": employees_db
    }

    # STEP-3 - Send context object through render() function
    return render(request, 'empapp/list_emp.html', context=context_data)


def delete_emp(request):
    if request.method == 'GET':
        return render(request, 'empapp/del_emp_form.html')
    elif request.method == 'POST':
        #step1 - read the input employee id to be deleted  3
        id_input = request.POST.get('emp_pk')

        #step2 - get Employee object from DB based on input employee id...
        try:
            employee = Employee.objects.get(id=id_input)
            employee.delete()
            resp_msg = '<h1 style = "color:green">Employee Deleted Successfully!!!</h1>'
        except Exception:
            resp_msg = '<h1 style = "color:red"> Sorry, Employee with id {} did not find in the DB!!</h1>'.format(id_input)
        return HttpResponse(resp_msg)

def ems(request):
    if request.method == 'GET':
        #step 1 : Get all employees
        employees_db = Employee.objects.all()

        context_data = {
            "employees": employees_db
        }
        return render(request, 'empapp/ems.html', context=context_data)
    elif request.method == 'POST':

        #step 1 : Read Employee input data

        empid = request.POST.get('emp_id')
        name = request.POST.get('emp_name')
        age = request.POST.get('emp_age')
        salary = request.POST.get('emp_salary')
        address = request.POST.get('emp_address')

        #step 2 : create "Employee Model" object using Employee input data

        employee = Employee(empid=empid, name=name, age=age, salary=salary, address=address)

        #step 3 : call save() method on " Employee Model" object

        employee.save()

        return redirect('/empapp/ems/')



def update_employee(request, pk):
    employee_db = Employee.objects.get(id=pk)

    employee_db.empid = request.POST.get("emp_id")
    employee_db.name = request.POST.get("emp_name")
    employee_db.age = request.POST.get("emp_age")
    employee_db.salary = request.POST.get("emp_salary")
    employee_db.address = request.POST.get("emp_address")

    employee_db.save()
    return redirect('/empapp/ems/')


def delete_employee(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/empapp/ems/')


