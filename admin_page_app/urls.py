from django.urls import path

from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list'),

    # Employer URLs
    path('employers/', views.EmployerListCreateAPIView.as_view(), name='employer-list'),
    # Language
    path('languages/', views.LanguagesListCreateAPIView.as_view(), name='language-list-create'),

    # Employee Card URLs
    path('employee_cards/', views.EmployeeCardListCreateAPIView.as_view(), name='employee-card-list'),

    # CV URLs
    path('cvs/', views.CVListCreateAPIView.as_view(), name='cv-list'),

    # Employee Passport URLs
    path('employee_passports/', views.EmployeePassportListCreateAPIView.as_view(), name='employee-passport-list'),

    # Category URLs
    path('category/', views.CategoryListCreateAPIView.as_view(), name='category-list'),

    # Order URLs
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list'),

    # Proposal URLs
    path('proposals/', views.ProposalsListCreateAPIView.as_view(), name='proposal-list'),

    # Job URLs
    path('jobs/', views.JobListCreateAPIView.as_view(), name='job-list'),

    # Job Appeal URLs
    path('job_appeals/', views.JobAppealListCreateAPIView.as_view(), name='job-appeal-list'),

    # Employee Review URLs
    path('employee_reviews/', views.EmployeeReviewListCreateAPIView.as_view(), name='employee-review-list'),

    # Employer Review URLs
    path('employer_reviews/', views.EmployerReviewListCreateAPIView.as_view(), name='employer-review-list'),

    # Payment URLs
    path('payments/', views.PaymentListCreateAPIView.as_view(), name='payment-list'),

    # Payment Appeal URLs
    path('payment_appeals/', views.PaymentAppealListCreateAPIView.as_view(), name='payment-appeal-list'),
]
