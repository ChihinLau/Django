from rest_framework import serializers
from .models import employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = employee
		fields = ["employee_id", "First_name", "Last_name", "Department", "Salary"]
"""
class EmployeeSerializer(serializers.Serializer):
	#id=serializers.IntegerField(primary_key = True)
	First_name=serializers.CharField(max_length=100)
	Last_name=serializers.CharField(max_length=100)
	Department=serializers.CharField(max_length=100)
	Salary=serializers.IntegerField ()

	def create(self, validated_data):
		return employee.objects.create(validated_data)

	def update(self, instance, validated_data):
		instance.First_name=validated_data.get("First_name", instance.First_name)
		instance.Last_name=validated_data.get("Last_name", instance.Last_name)
		instance.Department=validated_data.get("Department", instance.Department)
		instance.Salary=validated_data.get("Salary", instance.Salary)
		instance.save()
		return instance
"""