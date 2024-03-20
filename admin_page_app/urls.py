from django.urls import path
from . import views

urlpatterns = [
    # URLs for Employee model
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),

    # URLs for Employer model
    path('employers/', views.EmployerListCreate.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', views.EmployerRetrieveUpdateDestroy.as_view(), name='employer-retrieve-update-destroy'),

    # URLs for EmployeeCard model
    path('employeecards/', views.EmployeeCardListCreate.as_view(), name='employeecard-list-create'),
    path('employeecards/<int:pk>/', views.EmployeeCardRetrieveUpdateDestroy.as_view(), name='employeecard-retrieve-update-destroy'),

    # URLs for CV model
    path('cvs/', views.CVListCreate.as_view(), name='cv-list-create'),
    path('cvs/<int:pk>/', views.CVRetrieveUpdateDestroy.as_view(), name='cv-retrieve-update-destroy'),

    # URLs for EmployeePassport model
    path('employeepassports/', views.EmployeePassportListCreate.as_view(), name='employeepassport-list-create'),
    path('employeepassports/<int:pk>/', views.EmployeePassportRetrieveUpdateDestroy.as_view(), name='employeepassport-retrieve-update-destroy'),

    # URLs for EmployerPassport model
    path('employerpassports/', views.EmployerPassportListCreate.as_view(), name='employerpassport-list-create'),
    path('employerpassports/<int:pk>/', views.EmployerPassportRetrieveUpdateDestroy.as_view(), name='employerpassport-retrieve-update-destroy'),

    # URLs for Order model
    path('orders/', views.OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroy.as_view(), name='order-retrieve-update-destroy'),

    # URLs for Proposal model
    path('proposals/', views.ProposalListCreate.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', views.ProposalRetrieveUpdateDestroy.as_view(), name='proposal-retrieve-update-destroy'),

    # URLs for Job model
    path('jobs/', views.JobListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', views.JobRetrieveUpdateDestroy.as_view(), name='job-retrieve-update-destroy'),

    # URLs for JobAppeal model
    path('jobappeals/', views.JobAppealListCreate.as_view(), name='jobappeal-list-create'),
    path('jobappeals/<int:pk>/', views.JobAppealRetrieveUpdateDestroy.as_view(), name='jobappeal-retrieve-update-destroy'),

    # URLs for EmployeeReview model
    path('employeereviews/', views.EmployeeReviewListCreate.as_view(), name='employeereview-list-create'),
    path('employeereviews/<int:pk>/', views.EmployeeReviewRetrieveUpdateDestroy.as_view(), name='employeereview-retrieve-update-destroy'),

    # URLs for EmployerReview model
    path('employerreviews/', views.EmployerReviewListCreate.as_view(), name='employerreview-list-create'),
    path('employerreviews/<int:pk>/', views.EmployerReviewRetrieveUpdateDestroy.as_view(), name='employerreview-retrieve-update-destroy'),

    # URLs for Payment model
    path('payments/', views.PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', views.PaymentRetrieveUpdateDestroy.as_view(), name='payment-retrieve-update-destroy'),

    # URLs for PaymentAppeal model
    path('paymentappeals/', views.PaymentAppealListCreate.as_view(), name='paymentappeal-list-create'),
    path('paymentappeals/<int:pk>/', views.PaymentAppealRetrieveUpdateDestroy.as_view(), name='paymentappeal-retrieve-update-destroy'),
]
