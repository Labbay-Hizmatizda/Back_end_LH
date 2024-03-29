from django.contrib import admin

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'date_created')
    list_filter = ('name', 'surname')


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'date_created')
    list_filter = ('name', 'surname')


class EmployeeCardAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'card_holder', 'holder_name')
    list_filter = ('holder_name',)


class CVAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'media', 'bio', 'rating')
    list_filter = ('rating',)


class EmployeePassportAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'images_dir', 'is_approved')
    list_filter = ('is_approved',)




class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'category', 'description', 'media', 'location', 'location_link', 'price')
    list_filter = ('category', 'media')


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'order_id', 'price')
    list_filter = ('price',)


class JobAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'proposal_id', 'price', 'is_active')
    list_filter = ('is_active',)


class JobAppealAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'job_id', 'message')


class EmployeeReviewAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'owner_id', 'employer_id', 'rate')
    list_filter = ('rate',)


class EmployerReviewAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'owner_id', 'employee_id', 'rate')
    list_filter = ('rate',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'employee_approve', 'employer_approve')
    list_filter = ('employee_approve', 'employer_approve')


class PaymentAppealAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'payment_id', 'message')
    list_filter = ('owner_id',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(EmployeeCard, EmployeeCardAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(EmployeePassport, EmployeePassportAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Proposals, ProposalAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobAppeal, JobAppealAdmin)
admin.site.register(EmployeeReview, EmployeeReviewAdmin)
admin.site.register(EmployerReview, EmployerReviewAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentAppeal, PaymentAppealAdmin)
admin.site.register(Category)