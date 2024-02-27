from django.shortcuts import render
from .models import *

def admin_page_views(request):
    employees = Employee.objects.all()
    employers = Employer.objects.all()
    employee_cards = EmployeeCard.objects.all()
    cvs = CV.objects.all()
    employee_passports = EmployeePassport.objects.all()
    employer_passports = EmployerPassport.objects.all()
    orders = Order.objects.all()
    proposals = Proposal.objects.all()
    jobs = Job.objects.all()
    job_appeals = JobAppeal.objects.all()
    employee_appeals = EmployeeAppeal.objects.all()
    employer_appeals = EmployerAppeal.objects.all()
    payments = Payment.objects.all()
    payment_appeals = PaymentAppeal.objects.all()

    # Pass all instances to the template
    return render(request, 'admin.html', {
        'employees': employees,
        'employers': employers,
        'employee_cards': employee_cards,
        'cvs': cvs,
        'employee_passports': employee_passports,
        'employer_passports': employer_passports,
        'orders': orders,
        'proposals': proposals,
        'jobs': jobs,
        'job_appeals': job_appeals,
        'employee_appeals': employee_appeals,
        'employer_appeals': employer_appeals,
        'payments': payments,
        'payment_appeals': payment_appeals,
    })
