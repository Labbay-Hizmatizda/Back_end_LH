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
    owner = EmployeeSerializer()

    class Meta:
        model = EmployeeCard
        fields = '__all__'


class CVSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()

    class Meta:
        model = CV
        fields = '__all__'


class EmployeePassportSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()

    class Meta:
        model = EmployeePassport
        fields = '__all__'


class EmployerPassportSerializer(serializers.ModelSerializer):
    owner = EmployerSerializer()

    class Meta:
        model = EmployerPassport
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    owner = EmployerSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()
    order = OrderSerializer()

    class Meta:
        model = Proposal
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    proposal = ProposalSerializer()

    class Meta:
        model = Job
        fields = '__all__'


class JobAppealSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()
    job = JobSerializer()

    class Meta:
        model = JobAppeal
        fields = '__all__'


class EmployeeReviewSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    owner = EmployeeSerializer()
    employer = EmployerSerializer()

    class Meta:
        model = EmployeeReview
        fields = '__all__'


class EmployerReviewSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    owner = EmployerSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = EmployerReview
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    job = JobSerializer()

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAppealSerializer(serializers.ModelSerializer):
    owner = EmployerSerializer()
    payment = PaymentSerializer()

    class Meta:
        model = PaymentAppeal
        fields = '__all__'


