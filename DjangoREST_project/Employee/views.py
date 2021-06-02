from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from Employee.models import employee
from Employee.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
#@Employee(['GET', 'POST'])
def employee_list(request):
	if request.method == "GET":
		employees=employee.objects.all()
		serializer = EmployeeSerializer(employees, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = EmployeeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

