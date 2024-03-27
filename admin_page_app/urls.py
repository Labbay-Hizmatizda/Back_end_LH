from django.urls import path

from .views import (
    EmployeeListCreateAPIView, EmployeeDetailAPIView,
    EmployerListCreateAPIView, EmployerDetailAPIView,
    EmployeePassportListCreateAPIView, EmployeePassportDetailAPIView,
    OrderListCreateAPIView, OrderDetailAPIView,
    ProposalListCreateAPIView, ProposalDetailAPIView,
    JobListCreateAPIView, JobDetailAPIView,
    JobAppealListCreateAPIView, JobAppealDetailAPIView,
    EmployeeReviewListCreateAPIView, EmployeeReviewDetailAPIView,
    EmployerReviewListCreateAPIView, EmployerReviewDetailAPIView,
    PaymentListCreateAPIView, PaymentDetailAPIView,
    PaymentAppealListCreateAPIView, PaymentAppealDetailAPIView,
    CVListCreateAPIView, CVDetailAPIView, EmployeeCardListCreateAPIView, EmployeeCardDetailAPIView
)

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),

    path('employers/', EmployerListCreateAPIView.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', EmployerDetailAPIView.as_view(), name='employer-detail'),

    path('employee_passports/', EmployeePassportListCreateAPIView.as_view(), name='employee-passport-list-create'),
    path('employee_passports/<int:pk>/', EmployeePassportDetailAPIView.as_view(), name='employee-passport-detail'),

    path('employee_cards/', EmployeeCardListCreateAPIView.as_view(), name='employee-card-list-create'),
    path('employee_cards/<int:pk>/', EmployeeCardDetailAPIView.as_view(), name='employee-card-detail'),

    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),

    path('proposals/', ProposalListCreateAPIView.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', ProposalDetailAPIView.as_view(), name='proposal-detail'),

    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),

    path('job_appeals/', JobAppealListCreateAPIView.as_view(), name='job-appeal-list-create'),
    path('job_appeals/<int:pk>/', JobAppealDetailAPIView.as_view(), name='job-appeal-detail'),

    path('employee_reviews/', EmployeeReviewListCreateAPIView.as_view(), name='employee-review-list-create'),
    path('employee_reviews/<int:pk>/', EmployeeReviewDetailAPIView.as_view(), name='employee-review-detail'),

    path('employer_reviews/', EmployerReviewListCreateAPIView.as_view(), name='employer-review-list-create'),
    path('employer_reviews/<int:pk>/', EmployerReviewDetailAPIView.as_view(), name='employer-review-detail'),

    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),

    path('payment_appeals/', PaymentAppealListCreateAPIView.as_view(), name='payment-appeal-list-create'),
    path('payment_appeals/<int:pk>/', PaymentAppealDetailAPIView.as_view(), name='payment-appeal-detail'),

    path('cvs/', CVListCreateAPIView.as_view(), name='cv-list-create'),
    path('cvs/<int:pk>/', CVDetailAPIView.as_view(), name='cv-detail'),
]
