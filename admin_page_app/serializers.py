from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user_id', 'name', 'surname', 'phone_number', 'date_created']


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployeeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCard
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class EmployeePassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePassport
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class ProposalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposals
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAppeal
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class EmployeeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeReview
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class EmployerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerReview
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAppeal
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner_id'] = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        return data
