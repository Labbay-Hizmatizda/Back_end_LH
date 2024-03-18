# myapp/urls.py
from django.urls import path
from .views import (
    EmployeeListCreateAPIView, EmployeeDetailAPIView,
    EmployerListCreateAPIView, EmployerDetailAPIView,
    OrderListCreateAPIView, OrderDetailAPIView,
    ProposalListCreateAPIView, ProposalDetailAPIView,
    JobListCreateAPIView, JobDetailAPIView,
)

urlpatterns = [
    # Employee URLs
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),

    # Employer URLs
    path('employers/', EmployerListCreateAPIView.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', EmployerDetailAPIView.as_view(), name='employer-detail'),

    # Order URLs
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),

    # Proposal URLs
    path('proposals/', ProposalListCreateAPIView.as_view(), name='proposal-list-create'),
    path('proposals/<int:pk>/', ProposalDetailAPIView.as_view(), name='proposal-detail'),

    # Job URLs
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
]
