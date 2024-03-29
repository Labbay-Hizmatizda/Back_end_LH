from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployeeCardSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = EmployeeCard
        fields = '__all__'


class CVSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = CV
        fields = '__all__'


class EmployeePassportSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = EmployeePassport
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = Proposals
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobAppealSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = JobAppeal
        fields = '__all__'


class EmployeeReviewSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = EmployeeReview
        fields = '__all__'


class EmployerReviewSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = EmployerReview
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAppealSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField()

    class Meta:
        model = PaymentAppeal
        fields = '__all__'
