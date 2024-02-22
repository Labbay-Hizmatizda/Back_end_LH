from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)


class Employer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)


class EmployeeCard(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    holder_name = models.CharField(max_length=100)
    number = models.CharField(max_length=16)


class CV(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cv_images/')
    bio = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])


class EmployeePassport(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    personal_number = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)


class EmployerPassport(models.Model):
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
    personal_number = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)


class Order(models.Model):
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='order_images/')
    location = models.CharField(max_length=255)
    location_link = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Proposal(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Job(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)


class JobAppeal(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    message = models.TextField()


class EmployeeAppeal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    message = models.TextField()


class EmployerAppeal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    message = models.TextField()


class Payment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee_approve = models.BooleanField(default=False)
    employer_approve = models.BooleanField(default=False)


class PaymentAppeal(models.Model):
    owner = models.ForeignKey(models.Model, on_delete=models.CASCADE)  # Either Employee or Employer
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    message = models.TextField()
