from django.db import models


class Employee(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname} "


class Employer(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class EmployeeCard(models.Model):
    owner_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    holder_name = models.CharField(max_length=100)
    card_number = models.IntegerField(default=0,)


class CV(models.Model):
    owner_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    media = models.ImageField(upload_to="cv_images/")
    bio = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])


class EmployeePassport(models.Model):
    images_dir = models.ImageField(upload_to="passport_images/")
    owner_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    owner_id = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="orders")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    description = models.TextField()
    media = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    location_link = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)


class Proposals(models.Model):
    owner_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="proposals")
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Job(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="jobs")
    proposal_id = models.ForeignKey(Proposals, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)


class JobAppeal(models.Model):
    owner_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    message = models.TextField()


class EmployeeReview(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    message = models.TextField()


class EmployerReview(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    message = models.TextField()


class Payment(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee_approve = models.BooleanField(default=False)
    employer_approve = models.BooleanField(default=False)


class PaymentAppeal(models.Model):
    owner_id = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="payment_appeals")
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    message = models.TextField()
