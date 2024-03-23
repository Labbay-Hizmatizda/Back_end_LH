# serializers.py
from rest_framework import serializers

from .models import Employee, Employer, Order, Proposal, Job, JobAppeal, EmployeeReview, EmployerReview, Payment, \
    PaymentAppeal, EmployeePassport


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployeePassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePassport
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAppeal
        fields = '__all__'


class EmployeeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeReview
        fields = '__all__'


class EmployerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerReview
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAppeal
        fields = '__all__'
