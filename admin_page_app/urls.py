# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employers/', views.EmployerListCreateAPIView.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', views.EmployerDetailAPIView.as_view(), name='employer-detail'),
    path('employeepassports/', views.EmployeePassportListCreateAPIView.as_view(), name='employeepassport-list-create'),
    path('employeepassports/<int:pk>/', views.EmployeePassportDetailAPIView.as_view(), name='employeepassport-detail'),
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('proposals/', views.ProposalListCreateAPIView.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', views.ProposalDetailAPIView.as_view(), name='proposal-detail'),
    path('jobs/', views.JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', views.JobDetailAPIView.as_view(), name='job-detail'),
    path('jobappeals/', views.JobAppealListCreateAPIView.as_view(), name='jobappeal-list-create'),
    path('jobappeals/<int:pk>/', views.JobAppealDetailAPIView.as_view(), name='jobappeal-detail'),
    path('employeereviews/', views.EmployeeReviewListCreateAPIView.as_view(), name='employeereview-list-create'),
    path('employeereviews/<int:pk>/', views.EmployeeReviewDetailAPIView.as_view(), name='employeereview-detail'),
    path('employerreviews/', views.EmployerReviewListCreateAPIView.as_view(), name='employerreview-list-create'),
    path('employerreviews/<int:pk>/', views.EmployerReviewDetailAPIView.as_view(), name='employerreview-detail'),
    path('payments/', views.PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', views.PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('paymentappeals/', views.PaymentAppealListCreateAPIView.as_view(), name='paymentappeal-list-create'),
    path('paymentappeals/<int:pk>/', views.PaymentAppealDetailAPIView.as_view(), name='paymentappeal-detail'),
]
