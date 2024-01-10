import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee


def employee_crud(request, pk=None):
    if request.method == "GET":
        print('This is GET req')
        if pk is not None:
            # Get by Id
            # 1 .Get the employee details from DB based on PK value

            employee = Employee.objects.get(id=pk)
            # 2 . covertion - 1: convert model object into Dict (manual convertion)

            emp_dict ={

                "id": employee.id,
                "empid": employee.empid,
                "name": employee.name,
                "age": employee.age,
                "salary": employee.salary,
                "address": employee.address
                }

            # 2 .covertion -2: convert dict in json(dumps())

            emp_json = json.dumps(emp_dict)

            #emps_json_metadeta = serialize('json', [employee, ])
            #emps_json = parse_output(emps_json_metadeta)

            return HttpResponse(emp_json, content_type='application/json')

        else:
            # Get All
            employees_db = Employee.objects.all()
            emps_json_metadeta = serialize('json', employees_db)
            emps_json = parse_output(emps_json_metadeta)
            return HttpResponse(emps_json, content_type='application/json')

    elif request.method == 'POST':
        print("THis is POST req")

        ######          API
        # 1. read the incoming input data from the client
        emp_input_json = request.body

        # 2. convert JSON data into Dict object

        emp_input_dict = json.loads(emp_input_json)

        # 3, convert dict to Employee Model Object Manually

        empid = emp_input_dict.get('empid')
        name = emp_input_dict.get('name')
        age = emp_input_dict.get('age')
        salary = emp_input_dict.get('salary')
        address = emp_input_dict.get('address')
        employee = Employee(empid=empid, name=name, age=age, salary=salary, address=address)

        # 4 call save method on Employee Model so that data will be saved in db
        employee.save()

        # 5. send succes response to client

        res_dict = {'Message': "emp creted succesfully"}
        res_json = json.dumps(res_dict)

        return HttpResponse(res_json, content_type='application/json')

    elif request.method == "PUT":
        # 1. GET the input JSON from the request

        emp_in_json = request.body
        # 2. Convert JSOn into Dict
        emp_in_dict = json.loads(emp_in_json)

        # 3. GET emplloyee data from db

        emp_db = Employee.objects.get(id=pk)

        # 4. merge input data into db object

        emp_db.empid = emp_in_dict.get('empid')

        emp_db.name = emp_in_dict.get('name')
        emp_db.age = emp_in_dict.get('age')
        emp_db.salary = emp_in_dict.get('salary')
        emp_db.address = emp_in_dict.get('address')
        emp_db.save()

        # 5. send succes response to client

        res_dict = {'Message': "emp creted succesfully"}
        res_json = json.dumps(res_dict)

        return HttpResponse(res_json, content_type='application/json')

    elif request.method == 'DELETE':
        employee_db = Employee.objects.get(id=pk)
        employee_db.delete()

        resp_dict = {'message': 'Employee DELETED successfully!!!'}
        return HttpResponse(json.dumps(resp_dict), content_type="application/json")


def parse_output(employees_json_with_metadata):
    # Convert JSON into dict
    employees_dict_with_metadata = json.loads(employees_json_with_metadata)
    employee_list = []
    for emp_dict_with_metadata in employees_dict_with_metadata:
        employee = emp_dict_with_metadata['fields']
        employee['id'] = emp_dict_with_metadata['pk']
        employee_list.append(employee)

    employee_list_json = json.dumps(employee_list)
    return employee_list_json

