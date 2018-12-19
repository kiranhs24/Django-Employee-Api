from rest_framework import serializers
from . models import employee

class employeeSerializer(serializers.ModelSerializer):

    class Meta :

        model = employee
        #fields = ('firstname','lastname','emp_id')
        fields = '__all__'
        # serializers