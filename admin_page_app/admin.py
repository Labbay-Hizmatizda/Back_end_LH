from django.contrib import admin
from .models import Employee, Employer, EmployeeCard, CV, EmployeePassport, EmployerPassport
from .models import Order, Proposal, Job, JobAppeal, EmployeeReview, EmployerReview, Payment, PaymentAppeal

# Register your models here.

admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(EmployeeCard)
admin.site.register(CV)
admin.site.register(EmployeePassport)
# admin.site.register(EmployerPassport)

admin.site.register(Order)
admin.site.register(Proposal)
admin.site.register(Job)
admin.site.register(JobAppeal)
admin.site.register(EmployeeReview)
admin.site.register(EmployerReview)
admin.site.register(Payment)
admin.site.register(PaymentAppeal)
