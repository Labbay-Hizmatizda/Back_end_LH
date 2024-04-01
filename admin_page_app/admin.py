from django.contrib import admin

from .models import *


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'date_created')
    list_filter = ('name', 'surname')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'date_created')
    list_filter = ('name', 'surname')


@admin.register(EmployeeCard)
class EmployeeCardAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'card_holder', 'holder_name')


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'media', 'rating')


@admin.register(EmployeePassport)
class EmployeePassportAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'is_approved')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'category', 'description', 'price', 'is_active')


@admin.register(Proposals)
class ProposalsAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'order_id', 'price')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'proposal_id', 'price', 'is_active')


@admin.register(JobAppeal)
class JobAppealAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'job_id', 'message')


@admin.register(EmployeeReview)
class EmployeeReviewAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'owner_id', 'employer_id', 'rate')


@admin.register(EmployerReview)
class EmployerReviewAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'owner_id', 'employee_id', 'rate')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'employee_approve', 'employer_approve')


@admin.register(PaymentAppeal)
class PaymentAppealAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'payment_id', 'message')


admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(EmployeeCard)
admin.site.register(CV)
admin.site.register(EmployeePassport)
admin.site.register(Order)
admin.site.register(Proposals)
admin.site.register(Job)
admin.site.register(JobAppeal)
admin.site.register(EmployeeReview)
admin.site.register(EmployerReview)
admin.site.register(Payment)
admin.site.register(PaymentAppeal)
admin.site.register(Category)
