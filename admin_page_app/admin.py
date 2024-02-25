from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(EmployeeCard)
admin.site.register(CV)
admin.site.register(EmployeePassport)
admin.site.register(EmployerPassport)
admin.site.register(Order)
admin.site.register(Proposal)
admin.site.register(Job)
admin.site.register(JobAppeal)
admin.site.register(EmployeeAppeal)
admin.site.register(EmployerAppeal)
admin.site.register(Payment)
admin.site.register(PaymentAppeal)
