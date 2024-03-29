from django.urls import path

from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),

    # Employer URLs
    path('employers/', views.EmployerListCreateAPIView.as_view(), name='employer-list'),
    path('employers/<int:pk>/', views.EmployerReviewRetrieveUpdateDestroyAPIView.as_view(), name='employer-detail'),

    # Employee Card URLs
    path('employee_cards/', views.EmployeeCardListCreateAPIView.as_view(), name='employee-card-list'),
    path('employee_cards/<int:pk>/', views.EmployeeCardRetrieveUpdateDestroyAPIView.as_view(), name='employee-card-detail'),

    # CV URLs
    path('cvs/', views.CVListCreateAPIView.as_view(), name='cv-list'),
    path('cvs/<int:pk>/', views.CVRetrieveUpdateDestroyAPIView.as_view(), name='cv-detail'),

    # Employee Passport URLs
    path('employee_passports/', views.EmployeePassportListCreateAPIView.as_view(), name='employee-passport-list'),
    path('employee_passports/<int:pk>/', views.EmployeePassportRetrieveUpdateDestroyAPIView.as_view(), name='employee-passport-detail'),

    # Order URLs
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),

    # Proposal URLs
    path('proposals/', views.ProposalListCreateAPIView.as_view(), name='proposal-list'),
    path('proposals/<int:pk>/', views.ProposalRetrieveUpdateDestroyAPIView.as_view(), name='proposal-detail'),

    # Job URLs
    path('jobs/', views.JobListCreateAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', views.JobRetrieveUpdateDestroyAPIView.as_view(), name='job-detail'),

    # Job Appeal URLs
    path('job_appeals/', views.JobAppealListCreateAPIView.as_view(), name='job-appeal-list'),
    path('job_appeals/<int:pk>/', views.JobAppealRetrieveUpdateDestroyAPIView.as_view(), name='job-appeal-detail'),

    # Employee Review URLs
    path('employee_reviews/', views.EmployeeReviewListCreateAPIView.as_view(), name='employee-review-list'),
    path('employee_reviews/<int:pk>/', views.EmployeeReviewRetrieveUpdateDestroyAPIView.as_view(), name='employee-review-detail'),

    # Employer Review URLs
    path('employer_reviews/', views.EmployerReviewListCreateAPIView.as_view(), name='employer-review-list'),
    path('employer_reviews/<int:pk>/', views.EmployerReviewRetrieveUpdateDestroyAPIView.as_view(), name='employer-review-detail'),

    # Payment URLs
    path('payments/', views.PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),

    # Payment Appeal URLs
    path('payment_appeals/', views.PaymentAppealListCreateAPIView.as_view(), name='payment-appeal-list'),
    path('payment_appeals/<int:pk>/', views.PaymentAppealRetrieveUpdateDestroyAPIView.as_view(), name='payment-appeal-detail'),
]
