from rest_framework import serializers

from .models import Employee, Employer, EmployeeCard, CV, EmployeePassport, Order, Proposals, JobAppeal, \
    EmployeeReview, EmployerReview, Payment, PaymentAppeal, Job, Category, Languages


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.user_id = validated_data.get('user_id', instance.user_id)

        instance.save()
        return instance


class EmployeeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCard
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class EmployeePassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePassport
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employer.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class ProposalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposals
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAppeal
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class EmployeeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeReview
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employee.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employee.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class EmployerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerReview
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employer.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAppeal
        fields = '__all__'

    def get_owner_id(self, instance):
        owner = Employer.objects.get(id=instance.owner_id_id)
        return f"{owner.name} {owner.surname}"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        owner = Employer.objects.filter(id=instance.owner_id_id).values('name', 'surname').first()
        if owner:
            data['owner_id'] = f"{owner['name']} {owner['surname']}"
        return data


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'
