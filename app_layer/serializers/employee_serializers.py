from rest_framework import serializers
from app_layer.models.employee_models import Employee


class EmployeeSerializer(serializers.Serializer):
    empID = serializers.IntegerField(read_only=True)
    empName = serializers.CharField(required=True, max_length=100)
    empDescription = serializers.CharField(required=False, max_length=250, allow_blank=True)
    empCategory = serializers.CharField(required=False, max_length=250, allow_blank=True)
    empCity = serializers.CharField(required=True, max_length=50)
    empOfficeVenue = serializers.CharField(required=True, max_length=500)
    empDOJ = serializers.DateField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        try:
            return Employee.objects.create(**validated_data)
        except Exception as e:
            print(e)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.empName = validated_data.get('empName', instance.empName)
        instance.empDescription = validated_data.get('empDescription', instance.empDescription)
        instance.empCategory = validated_data.get('empCategory', instance.empCategory)
        instance.empCity = validated_data.get('empCity', instance.empCity)
        instance.empOfficeVenue = validated_data.get('empOfficeVenue', instance.empOfficeVenue)
        instance.empDOJ = validated_data.get('empDOJ', instance.empDOJ)
        instance.save()
        return instance


# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']