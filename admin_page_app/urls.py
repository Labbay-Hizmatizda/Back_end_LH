from django.urls import path
from .views import (
    EmployeeListCreate, EmployeeRetrieveUpdateDestroy,
    EmployerListCreate, EmployerRetrieveUpdateDestroy,
    EmployeeCardListCreate, EmployeeCardRetrieveUpdateDestroy,
    CVListCreate, CVRetrieveUpdateDestroy,
    EmployeePassportListCreate, EmployeePassportRetrieveUpdateDestroy,
    OrderListCreate, OrderRetrieveUpdateDestroy,
    ProposalListCreate, ProposalRetrieveUpdateDestroy,
    JobListCreate, JobRetrieveUpdateDestroy,
    JobAppealListCreate, JobAppealRetrieveUpdateDestroy,
    EmployeeReviewListCreate, EmployeeReviewRetrieveUpdateDestroy,
    EmployerReviewListCreate, EmployerReviewRetrieveUpdateDestroy,
    PaymentListCreate, PaymentRetrieveUpdateDestroy,
    PaymentAppealListCreate, PaymentAppealRetrieveUpdateDestroy,

)

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),

    path('employers/', EmployerListCreate.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', EmployerRetrieveUpdateDestroy.as_view(), name='employer-retrieve-update-destroy'),

    path('employeecards/', EmployeeCardListCreate.as_view(), name='employeecard-list-create'),
    path('employeecards/<int:pk>/', EmployeeCardRetrieveUpdateDestroy.as_view(), name='employeecard-retrieve-update-destroy'),

    path('cvs/', CVListCreate.as_view(), name='cv-list-create'),
    path('cvs/<int:pk>/', CVRetrieveUpdateDestroy.as_view(), name='cv-retrieve-update-destroy'),

    path('employeepassports/', EmployeePassportListCreate.as_view(), name='employeepassport-list-create'),
    path('employeepassports/<int:pk>/', EmployeePassportRetrieveUpdateDestroy.as_view(), name='employeepassport-retrieve-update-destroy'),

    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-retrieve-update-destroy'),

    path('proposals/', ProposalListCreate.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', ProposalRetrieveUpdateDestroy.as_view(), name='proposal-retrieve-update-destroy'),

    path('jobs/', JobListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDestroy.as_view(), name='job-retrieve-update-destroy'),

    path('jobappeals/', JobAppealListCreate.as_view(), name='jobappeal-list-create'),
    path('jobappeals/<int:pk>/', JobAppealRetrieveUpdateDestroy.as_view(), name='jobappeal-retrieve-update-destroy'),

    path('employeereviews/', EmployeeReviewListCreate.as_view(), name='employeereview-list-create'),
    path('employeereviews/<int:pk>/', EmployeeReviewRetrieveUpdateDestroy.as_view(), name='employeereview-retrieve-update-destroy'),

    path('employerreviews/', EmployerReviewListCreate.as_view(), name='employerreview-list-create'),
    path('employerreviews/<int:pk>/', EmployerReviewRetrieveUpdateDestroy.as_view(), name='employerreview-retrieve-update-destroy'),

    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-retrieve-update-destroy'),

    path('paymentappeals/', PaymentAppealListCreate.as_view(), name='paymentappeal-list-create'),
    path('paymentappeals/<int:pk>/', PaymentAppealRetrieveUpdateDestroy.as_view(), name='paymentappeal-retrieve-update-destroy'),
]
