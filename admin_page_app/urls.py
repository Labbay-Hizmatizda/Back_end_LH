# main/urls.py

from django.urls import path

from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployerListView,
    EmployerDetailView,
    EmployeeCardListView,
    CVListView,
    EmployeePassportListView,
    EmployerPassportListView,
    OrderListView,
    ProposalListView,
    JobListView,
    JobAppealListView,
    EmployeeReviewListView,
    EmployerReviewListView,
    PaymentListView,
    PaymentAppealListView,
)

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('employers/', EmployerListView.as_view(), name='employer-list'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),

    path('employeecards/', EmployeeCardListView.as_view(), name='employeecard-list'),
    path('cvs/', CVListView.as_view(), name='cv-list'),
    path('employeepassports/', EmployeePassportListView.as_view(), name='employeepassport-list'),
    path('employerpassports/', EmployerPassportListView.as_view(), name='employerpassport-list'),

    path('orders/', OrderListView.as_view(), name='order-list'),
    path('proposals/', ProposalListView.as_view(), name='proposal-list'),
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobappeals/', JobAppealListView.as_view(), name='jobappeal-list'),

    path('employeereviews/', EmployeeReviewListView.as_view(), name='employeereview-list'),
    path('employerreviews/', EmployerReviewListView.as_view(), name='employerreview-list'),

    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('paymentappeals/', PaymentAppealListView.as_view(), name='paymentappeal-list'),
]
